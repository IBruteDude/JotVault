from flask import jsonify, abort, request
import flask as fk
from sqlalchemy.sql import text
from sqlalchemy.exc import OperationalError

from api.v1.views import app_bp
from db import main_storage
from db.db_classes import User, Note


@app_bp.route('/<user_id>/notes',
             methods=['GET', 'POST'], strict_slashes=False)
def user_notes_route(user_id, note_id=None):
    user = main_storage.get(User, user_id)
    if user is None:
        return jsonify({'error': 'user not found'})

    match request.method:
        case 'GET':
            return jsonify([note.dict_repr() for note in user.notes])
        case 'POST':
            task_dict = request.get_json(silent=True)
            try:
                task = Note(**task_dict)
                main_storage.new(task)
                main_storage.save()
                return jsonify(task.dict_repr())
            except OperationalError:
                return jsonify({'error': 'json missing note parameters'})
            except Exception as e:
                print(f"[{e.__class__.__name__}]: {e}")
                return jsonify({})


@app_bp.route('/<user_id>/notes/<note_id>',
             methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def user_note_route(user_id, note_id):
    if main_storage.get(User, user_id) is None:
        return jsonify({'error': 'user not found'})

    note = main_storage.get(Note, note_id)
    if note is None or note.user_id != user_id:
        return jsonify({'error': 'note not found'})

    if request.method == 'GET':
        return jsonify(note.dict_repr())
    elif request.method == 'PUT':
        dic = request.get_json(silent=True)
        if type(dic) is dict:
            note.update(dic)
            return jsonify(note.dict_repr())
    elif request.method == 'DELETE':
        with main_storage.engine.connect() as con:
            con.execute(text(f"DELETE FROM notes WHERE id = '{note_id}';"))
            con.commit()
        main_storage.save()
        return jsonify({})


@app_bp.route('/<user_id>/notes/<note_id>/changes/<change_id>',
             methods=['GET'], strict_slashes=False)
def user_note_changes_route(user_id, note_id, change_id=None):
    return jsonify({'error': 'not implemented yet'})


@app_bp.route('/<user_id>/notes/<note_id>/content',
             methods=['GET'], strict_slashes=False)
def user_note_contents_route(user_id, note_id):
    return jsonify({'error': 'not implemented yet'})


@app_bp.route('/<user_id>/notes/<note_id>/changes/<change_id>/content',
             methods=['GET'], strict_slashes=False)
def user_note_changes_contents_route(user_id, note_id, change_id=None):
    return jsonify({'error': 'not implemented yet'})
