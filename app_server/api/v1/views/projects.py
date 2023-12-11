from flask import jsonify, abort, request
import flask as fk
from sqlalchemy.exc import OperationalError
import sqlalchemy.orm.collections as soc



from api.v1.views import app_bp
from db import main_storage
from db.db_classes import User, Project, Task, Note


@app_bp.route('/<user_id>/projects',
             methods=['GET', 'POST'], strict_slashes=False)
def user_projects_viewer(user_id):
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
                return jsonify(project.dict_repr())
            except OperationalError:
                return jsonify({'error': 'json missing project parameters'})
            except Exception as e:
                print(f"[{e.__class__.__name__}]: {e}")
                return jsonify({})

@app_bp.route('/<user_id>/projects/<project_id>',
             methods=['PUT', 'DELETE'], strict_slashes=False)
def user_projects_modifier(user_id, project_id):
    user = main_storage.get(User, user_id)
    if user is None:
        return jsonify({'error': 'user not found'})

    project = main_storage.get(Project, project_id)
    if project is None or project.user_id != user.id:
        return jsonify({'error': 'project not found'})
    match request.method:
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
def user_project_tasks_viewer(user_id, project_id):
    user = main_storage.get(User, user_id)
    if user is None:
        return jsonify({'error': 'user not found'})

    project = main_storage.get(Project, project_id)
    if project is None or project.user_id != user.id:
        return jsonify({'error': 'project not found'})
    match request.method:
        case 'GET':
            return jsonify([task.dict_repr() for task in project.tasks])
        case 'POST':
            try:
                task_dict = request.get_json(silent=True)
                # ensure correct user id
                task_dict['user_id'] = user_id
                task = Task(**task_dict)
                project.tasks.append(task)
                main_storage.save()
                return jsonify(task.dict_repr())
            except OperationalError:
                return jsonify({'error': 'json missing project parameters'})
            except Exception as e:
                print(f"[{e.__class__.__name__}]: {e}")
                return jsonify({})


@app_bp.route('/<user_id>/projects/<project_id>/tasks/<task_id>',
             methods=['PUT', 'DELETE'], strict_slashes=False)
def user_project_tasks_modifier(user_id, project_id, task_id):
    user = main_storage.get(User, user_id)
    if user is None:
        return jsonify({'error': 'user not found'})

    project = main_storage.get(Project, project_id)
    if project is None or project.user_id != user.id:
        return jsonify({'error': 'project not found'})

    task = main_storage.get(Task, task_id)
    if task not in project.tasks or task.user_id != user_id:
        return jsonify({'error': 'task not found'})

    match request.method:
        case 'PUT':
            dic = request.get_json(silent=True)
            if type(dic) is dict:
                task.update(dic)
                return jsonify(task.dict_repr())
            return jsonify({})
        case 'DELETE':
            main_storage.delete(task)
            main_storage.save()
            return jsonify({})



@app_bp.route('/<user_id>/projects/<project_id>/notes',
             methods=['GET', 'POST'], strict_slashes=False)
def user_project_notes_viewer(user_id, project_id):
    user = main_storage.get(User, user_id)
    if user is None:
        return jsonify({'error': 'user not found'})

    project = main_storage.get(Project, project_id)
    if project is None or project.user_id != user.id:
        return jsonify({'error': 'project not found'})

    match request.method:
        case 'GET':
            return jsonify([note.dict_repr() for note in project.notes])
        case 'POST':
            try:
                note_dict = request.get_json(silent=True)
                # ensure correct user id
                note_dict['user_id'] = user_id
                note = Task(**note_dict)
                project.notes.append(note)
                main_storage.save()
                return jsonify(note.dict_repr())
            except OperationalError:
                return jsonify({'error': 'json missing project parameters'})
            except Exception as e:
                print(f"[{e.__class__.__name__}]: {e}")
                return jsonify({})

@app_bp.route('/<user_id>/projects/<project_id>/notes/<note_id>',
             methods=['PUT', 'DELETE'], strict_slashes=False)
def user_project_notes_modifier(user_id, project_id, note_id):
    pass
