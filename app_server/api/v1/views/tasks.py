from flask import jsonify, abort, request
import flask as fk
from sqlalchemy.exc import OperationalError

from api.v1.views import app_bp
from db import main_storage
from db.db_classes import User, Task


@app_bp.route('/<user_id>/tasks',
             methods=['GET', 'POST'], strict_slashes=False)
def user_tasks_route(user_id):
    user = main_storage.get(User, user_id)
    if user is None:
        return jsonify({'error': 'user not found'})

    if request.method == 'GET':
        task_dicts = [task.dict_repr() for task in user.tasks]
        for task in task_dicts:
            task['start'] = str(task['start'])
            task['end'] = str(task['end'])
        return jsonify(task_dicts)
    elif request.method == 'POST':
        task_dict = request.get_json(silent=True)
        try:
            task = Task(**task_dict)
            main_storage.new(task)
            main_storage.save()
            task = task.dict_repr()
            task['start'] = str(task['start'])
            task['end'] = str(task['end'])
            return jsonify(task)
        except OperationalError:
            return jsonify({'error': 'json missing task parameters'})
        except Exception as e:
            print(f"[{e.__class__.__name__}]: {e}")
            return jsonify({})


@app_bp.route('/<user_id>/tasks/<task_id>',
             methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def user_task_route(user_id, task_id):
    user = main_storage.get(User, user_id)
    if user is None:
        return jsonify({'error': 'user not found'})

    task = main_storage.get(Task, task_id)
    if task is None or task.user_id != user.id:
        return jsonify({'error': 'task not found'})

    if request.method == 'GET':
        return jsonify(task.dict_repr())
    elif request.method == 'PUT':
        dic = request.get_json(silent=True)
        if type(dic) is dict:
            task.update(dic)
            return jsonify(task.dict_repr())
    elif request.method == 'DELETE':
        main_storage.delete(task)
        main_storage.save()
        return jsonify({})
