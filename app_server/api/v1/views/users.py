from flask import jsonify, abort, request
import flask as fk
from sqlalchemy.exc import OperationalError
from sqlalchemy.sql import text

from api.v1.views import app_bp
from db import main_storage
from db.db_classes import User
from utils.hash_algo import hash_password


@app_bp.route('/users',
              methods=['GET', 'POST'], strict_slashes=False)
def users_route():
    if request.method == 'GET':
        users = main_storage.all(User)
        for user in users:
            del user['password']
        return jsonify(users)
    elif request.method == 'POST':
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
              methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def user_route(user_id):
    user = main_storage.get(User, user_id)
    if user is None:
        return jsonify({'error': 'user not found'})

    if request.method == 'GET':
        user_dict = user.dict_repr()
        del user_dict['password']
        return jsonify(user_dict)
    elif request.method == 'PUT':
        dic = request.get_json(silent=True)
        if type(dic) is dict:
            if dic.get('password'):
                password = dic['password']
                dic['password'] = hash_password(dic['password'])
                user.update(dic)
                new_dic = main_storage.get(User, user_id).dict_repr()
                if hash_password(password) != new_dic['password']:
                    return jsonify({'error': 'error updating instance password'})
                new_dic['password'] = password
                dic = new_dic
            else:
                user.update(dic)
            return jsonify(dic)
        return jsonify({})
    elif request.method == 'DELETE':
        if user_id == '00000000-0000-0000-0000-000000000000':
            return jsonify({'error': f'cannot delete id {user_id}'})
        with main_storage.engine.connect() as con:
            con.execute(text(f"DELETE FROM users WHERE id = '{user_id}';"))
            con.commit()
        # main_storage.delete(user)
        main_storage.save()
        # assert main_storage.get(User, user_id) is None
        return jsonify({})
