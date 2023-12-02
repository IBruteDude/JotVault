from api.v1.views import app_bp
from flask import jsonify, abort
from db import main_storage
from db.db_classes import User, Note, NotesChangelog

@app_bp.route('/users',
             methods=['GET', 'POST'], strict_slashes=False)
def users_viewer():
    users = main_storage.all(User)
    for user in users:
        del user['password']
    return jsonify(users)

@app_bp.route('/users/<user_id>',
             methods=['PUT', 'DELETE'], strict_slashes=False)
def users_modifier(user_id):
    pass
