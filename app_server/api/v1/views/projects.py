from flask import jsonify, abort, request
import flask as fk
from sqlalchemy.sql import text
from sqlalchemy.exc import OperationalError
import sqlalchemy.orm.collections as soc

from api.v1.views import app_bp
from db import main_storage
from db.db_classes import User, Project, Task, Note


@app_bp.route('/<user_id>/projects',
             methods=['GET', 'POST'], strict_slashes=False)
def user_projects_route(user_id):
    user = main_storage.get(User, user_id)
    if user is None:
        return jsonify({'error': 'user not found'})

    match request.method:
        case 'GET':
            return jsonify([project.dict_repr() for project in user.projects])
        case 'POST':
            project_dict = request.get_json(silent=True)
            try:
                project = Project(**project_dict)
                main_storage.new(project)
                main_storage.save()
                return jsonify(project.dict_repr())
            except OperationalError:
                return jsonify({'error': 'json missing project parameters'})
            except Exception as e:
                print(f"[{e.__class__.__name__}]: {e}")
                return jsonify({})


@app_bp.route('/<user_id>/projects/<project_id>',
             methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def user_project_route(user_id, project_id):
    user = main_storage.get(User, user_id)
    if user is None:
        return jsonify({'error': 'user not found'})

    project = main_storage.get(Project, project_id)
    if project is None or project.user_id != user.id:
        return jsonify({'error': 'project not found'})
    match request.method:
        case 'GET':
            return jsonify(project.dict_repr())
        case 'PUT':
            dic = request.get_json(silent=True)
            if type(dic) is dict:
                project.update(dic)
                return jsonify(project.dict_repr())
        case 'DELETE':
            main_storage.delete(project)
            main_storage.save()
            return jsonify({})


@app_bp.route('/<user_id>/projects/<project_id>/tasks',
             methods=['GET', 'POST'], strict_slashes=False)
def user_project_tasks_route(user_id, project_id):
    user = main_storage.get(User, user_id)
    if user is None:
        return jsonify({'error': 'user not found'})

    project = main_storage.get(Project, project_id)

    if project is None or project.user_id != user.id:
        return jsonify({'error': 'project not found'})
    if request.method == 'GET':
        return jsonify([task.dict_repr() for task in project.tasks])
    elif request.method == 'POST':
        try:
            task_dict = request.get_json(silent=True)
            # ensure correct user id and project id
            task_dict['user_id'] = user_id
            task_dict['project_id'] = project_id
            task = Task(**task_dict)
            main_storage.new(task)
            main_storage.save()
            return jsonify(task.dict_repr())
        except OperationalError:
            return jsonify({'error': 'json missing project parameters'})
        except Exception as e:
            print(f"[{e.__class__.__name__}]: {e}")
            return jsonify({})


@app_bp.route('/<user_id>/projects/<project_id>/tasks/<task_id>',
             methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def user_project_task_route(user_id, project_id, task_id):
    user = main_storage.get(User, user_id)
    if user is None:
        return jsonify({'error': 'user not found'})

    project = main_storage.get(Project, project_id)
    if project is None or project.user_id != user.id:
        return jsonify({'error': 'project not found'})

    task = main_storage.get(Task, task_id)
    if task not in project.tasks or task.user_id != user_id:
        return jsonify({'error': 'task not found'})

    if request.method == 'GET':
        return jsonify(task.dict_repr())
    elif request.method == 'PUT':
        dic = request.get_json(silent=True)
        ##### THIS LEVEL OF INPUT HANDLING NEEDS TO BE ADDED OVER ALL ROUTES
        if type(dic) is not dict:
            return jsonify({'error': 'invalid request'})
        task.update(dic)
        return jsonify(task.dict_repr())
    elif request.method == 'DELETE':
        main_storage.delete(task)
        main_storage.save()
        if main_storage.get(Task, user_id) is not None:
            return jsonify({'error': 'there was a problem deleting the instance'})
        return jsonify({})


@app_bp.route('/<user_id>/projects/<project_id>/notes',
             methods=['GET', 'POST'], strict_slashes=False)
def user_project_notes_route(user_id, project_id):
    user = main_storage.get(User, user_id)
    if user is None:
        return jsonify({'error': 'user not found'})

    project = main_storage.get(Project, project_id)

    if project is None or project.user_id != user.id:
        return jsonify({'error': 'project not found'})

    if request.method == 'GET':
        return jsonify([note.dict_repr() for note in project.notes])
    elif request.method == 'POST':
        try:
            note_dict = request.get_json(silent=True)
            # ensure correct user id and project id
            note_dict['user_id'] = user_id
            note_dict['project_id'] = project_id
            note = Note(**note_dict)
            main_storage.new(note)
            main_storage.save()
            return jsonify(note.dict_repr())
        except OperationalError:
            return jsonify({'error': 'json missing project parameters'})
        except Exception as e:
            print(f"[{e.__class__.__name__}]: {e}")
            return jsonify({})


@app_bp.route('/<user_id>/projects/<project_id>/notes/<note_id>',
             methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def user_project_note_route(user_id, project_id, note_id):
    user = main_storage.get(User, user_id)
    if user is None:
        return jsonify({'error': 'user not found'})

    project = main_storage.get(Project, project_id)
    if project is None or project.user_id != user.id:
        return jsonify({'error': 'project not found'})

    note = main_storage.get(Note, note_id)
    if note is None or note.user_id != user_id or note.project_id != project_id:
        return jsonify({'error': 'note not found'})

    if request.method == 'GET':
        return jsonify(note.dict_repr())
    elif request.method == 'PUT':
        dic = request.get_json(silent=True)
        if type(dic) is dict:
            note.update(dic)
            return jsonify(note.dict_repr())
        return jsonify({})
    elif request.method == 'DELETE':
        with main_storage.engine.connect() as con:
            con.execute(text(f"DELETE FROM notes WHERE id = '{note_id}';"))
            con.commit()
        main_storage.save()
        return jsonify({})
