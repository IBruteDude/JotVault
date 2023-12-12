from flask import jsonify, abort, request
import flask as fk
from sqlalchemy.exc import OperationalError

from api.v1.views import app_bp
from db import main_storage
from db.db_classes import User, Task

@app_bp.route('/<user_id>/tasks',
             methods=['GET', 'POST'], strict_slashes=False)
def user_tasks_viewer(user_id):
    user = main_storage.get(User, user_id)
    if user is None:
        return jsonify({'error': 'user not found'})

    match request.method:
        case 'GET':
            return jsonify([task.dict_repr() for task in user.tasks])
        case 'POST':
            task_dict = request.get_json(silent=True)
            try:
                task = Task(**task_dict)
                main_storage.new(task)
                return jsonify(task.dict_repr())
            except OperationalError:
                return jsonify({'error': 'json missing task parameters'})

@app_bp.route('/<user_id>/tasks/<task_id>',
             methods=['PUT', 'DELETE'], strict_slashes=False)
def user_tasks_modifier(user_id, task_id):
    user = main_storage.get(User, user_id)
    if user is None:
        return jsonify({'error': 'user not found'})

    task = main_storage.get(Task, task_id)
    if task is None or task.user_id != user.id:
        return jsonify({'error': 'task not found'})
    match request.method:
        case 'PUT':
            dic = request.get_json(silent=True)
            if type(dic) is dict:
                task.update(dic)
                return jsonify(task.dict_repr())
        case 'DELETE':
            main_storage.delete(task)
            main_storage.save()
            return jsonify({})
