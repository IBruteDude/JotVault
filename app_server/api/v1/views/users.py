from flask import jsonify, abort, request
import flask as fk
from sqlalchemy.exc import OperationalError

from api.v1.views import app_bp
from db import main_storage
from db.db_classes import User

@app_bp.route('/users',
              methods=['GET', 'POST'], strict_slashes=False)
def users_viewer():
    match request.method:
        case 'GET':
            users = main_storage.all(User)
            for user in users:
                del user['password']
            return jsonify(users)
        case 'POST':
            user_dict = request.get_json(silent=True)
            try:
                user = User(**user_dict)
                main_storage.new(user)
                main_storage.save()
                dic = user.dict_repr()
                dic['password'] = user_dict['password']
                return jsonify(dic)
            except OperationalError:
                return jsonify({'error': 'json missing user parameters'})
            except Exception as e:
                print(f"[{e.__class__.__name__}]: {e}")
                return jsonify({})

@app_bp.route('/users/<user_id>',
              methods=['PUT', 'DELETE'], strict_slashes=False)
def users_modifier(user_id):
    user = main_storage.get(User, user_id)
    if user is None:
        return jsonify({'error': 'user not found'})
    match request.method:
        case 'PUT':
            dic = request.get_json(silent=True)
            if type(dic) is dict:
                user.update(dic)
                return jsonify(user.dict_repr())
            return jsonify({})
        case 'DELETE':
            main_storage.delete(user)
            main_storage.save()
            return jsonify({})
