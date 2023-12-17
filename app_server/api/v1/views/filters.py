from flask import jsonify, abort, request
import flask as fk
from sqlalchemy.exc import OperationalError

from api.v1.views import app_bp
from db import main_storage
from db.db_classes import User, Note, Task


@app_bp.route('/<user_id>/notes/pinned',
             methods=['GET'], strict_slashes=False)
def user_pinned_notes_route(user_id):
    if main_storage.get(User, user_id) is None:
        return jsonify({'error': 'user not found'})
    pinned_notes = main_storage.session.query(Note).where(Note.status == "pinned").all()
    return jsonify([note.dict_repr() for note in pinned_notes])


@app_bp.route('/<user_id>/notes/normal',
             methods=['GET'], strict_slashes=False)
def user_normal_notes_route(user_id):
    if main_storage.get(User, user_id) is None:
        return jsonify({'error': 'user not found'})
    normal_notes = main_storage.session.query(Note).where(Note.status == "normal").all()
    return jsonify([note.dict_repr() for note in normal_notes])


@app_bp.route('/<user_id>/notes/archived',
             methods=['GET'], strict_slashes=False)
def user_archived_notes_route(user_id):
    if main_storage.get(User, user_id) is None:
        return jsonify({'error': 'user not found'})
    archived_notes = main_storage.session.query(Note).where(Note.status == "archived").all()
    return jsonify([note.dict_repr() for note in archived_notes])


@app_bp.route('/<user_id>/notes/trashed',
             methods=['GET'], strict_slashes=False)
def user_trashed_notes_route(user_id):
    if main_storage.get(User, user_id) is None:
        return jsonify({'error': 'user not found'})
    trashed_notes = main_storage.session.query(Note).where(Note.status == "trashed").all()
    return jsonify([note.dict_repr() for note in trashed_notes])




@app_bp.route('/<user_id>/tasks/todo',
             methods=['GET'], strict_slashes=False)
def user_todo_tasks_route(user_id):
    if main_storage.get(User, user_id) is None:
        return jsonify({'error': 'user not found'})
    todo_tasks = main_storage.session.query(Task).where(Task.status == "todo").all()
    return jsonify([task.dict_repr() for task in todo_tasks])


@app_bp.route('/<user_id>/tasks/doing',
             methods=['GET'], strict_slashes=False)
def user_doing_tasks_route(user_id):
    if main_storage.get(User, user_id) is None:
        return jsonify({'error': 'user not found'})
    doing_tasks = main_storage.session.query(Task).where(Task.status == "doing").all()
    return jsonify([task.dict_repr() for task in doing_tasks])


@app_bp.route('/<user_id>/tasks/done',
             methods=['GET'], strict_slashes=False)
def user_done_tasks_route(user_id):
    if main_storage.get(User, user_id) is None:
        return jsonify({'error': 'user not found'})
    done_tasks = main_storage.session.query(Task).where(Task.status == "done").all()
    return jsonify([task.dict_repr() for task in done_tasks])
