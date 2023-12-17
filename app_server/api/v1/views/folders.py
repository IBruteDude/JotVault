from flask import jsonify, abort, request
import flask as fk
from sqlalchemy.exc import OperationalError

from api.v1.views import app_bp
from db import main_storage
from db.db_classes import User, Folder


@app_bp.route('/<user_id>/folders',
             methods=['GET', 'POST'], strict_slashes=False)
def user_folders_route(user_id):
    user = main_storage.get(User, user_id)
    if user is None:
        return jsonify({'error': 'user not found'})

    if request.method == 'GET':
        return jsonify([folder.dict_repr() for folder in user.folders])
    elif request.method == 'POST':
        folder_dict = request.get_json(silent=True)
        try:
            folder = Folder(**folder_dict)
            main_storage.new(folder)
            main_storage.save()
            return jsonify(folder.dict_repr())
        except OperationalError:
            return jsonify({'error': 'json missing folder parameters'})


@app_bp.route('/<user_id>/folders/<folder_id>',
              methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def user_folder_route(user_id, folder_id):
    user = main_storage.get(User, user_id)
    if user is None:
        return jsonify({'error': 'user not found'})

    folder = main_storage.get(Folder, folder_id)
    if folder is None or folder.user_id != user.id:
        return jsonify({'error': 'folder not found'})
    if request.method == 'GET':
        return jsonify(folder.dict_repr())
    elif request.method == 'PUT':
        dic = request.get_json(silent=True)
        if type(dic) is dict:
            folder.update(dic)
            return jsonify(folder.dict_repr())
        return jsonify({})
    elif request.method == 'DELETE':
        if folder_id == '00000000-0000-0000-0000-000000000000':
            return jsonify({'error': f'cannot delete id {folder_id}'})
        main_storage.delete(folder)
        main_storage.save()
        return jsonify({})
