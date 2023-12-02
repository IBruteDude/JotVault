from api.v1.views import app_bp
from flask import jsonify, abort
from db import main_storage
from db.db_classes import User, Note, NotesChangelog


@app_bp.route('/<user_id>/notes',
             methods=['GET', 'POST', 'PUT', 'DELETE'], strict_slashes=False)
def user_notes(user_id, note_id=None):
    user = main_storage.get(User, user_id)
    if user is None:
        return jsonify({'error': f"user {user_id} doesn't exist"})
    return jsonify([note.dict_repr() for note in user.notes])

@app_bp.route('/<user_id>/notes/<note_id>/changes/<change_id>',
             methods=['GET'], strict_slashes=False)
def user_note_changes(user_id, note_id, change_id=None):
    pass

@app_bp.route('/<user_id>/notes/<note_id>/content',
             methods=['GET', 'POST', 'PUT', 'DELETE'], strict_slashes=False)
def user_note_contents(user_id, note_id):
    pass

@app_bp.route('/<user_id>/notes/<note_id>/changes/<change_id>/content',
             methods=['GET', 'POST', 'PUT', 'DELETE'], strict_slashes=False)
def user_note_changes_contents(user_id, note_id, change_id=None):
    pass
