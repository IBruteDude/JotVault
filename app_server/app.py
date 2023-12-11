#!/usr/bin/env python
from json import load
from os import getcwd

from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

from db import main_storage
import api.v1.views
from api.v1.views import app_bp

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

from db import main_storage
from db.db_classes import User, Note, NotesChangelog

react_folder = '../frontend/'
build_dir = f'{getcwd()}/{react_folder}/build'
asset_dir = f'{build_dir}/static'


@app.route('/')
def index():
    return send_from_directory(directory=build_dir, path='index.html')


@app.route('/static/<folder>/<file>')
def static_content(folder, file):
    filepath = f'{folder}/{file}'
    return send_from_directory(directory=asset_dir, path=filepath)

app.register_blueprint(app_bp)

@app.teardown_appcontext
def close_session(teardown_error):
    main_storage.close()

if __name__ == '__main__':
    try:
        app.run(host="0.0.0.0", port="5000", debug=True)
    except Exception as e:
        print(f'[{e.__class__.__name__}]: {e.args}')
