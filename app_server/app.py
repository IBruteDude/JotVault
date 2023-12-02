#!/usr/bin/env python
from flask import Flask, jsonify
from flask_cors import CORS
from db import main_storage
import api.v1.views
from api.v1.views import app_bp
from json import load

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

from db import main_storage
from db.db_classes import User, Note, NotesChangelog

@app_bp.route('/')
def index():
    return "what is up jotty boi"
    return jsonify(str(main_storage.all(User)))
# str(main_storage.get(User, '620ed68c-90e0-11ee-b4cd-00155db5b53c').notes)

app.register_blueprint(app_bp)

@app.teardown_appcontext
def close_session(teardown_error):
    main_storage.close()

if __name__ == '__main__':
    try:
        app.run(host="0.0.0.0", port="5000", debug=True)
    except Exception as e:
        print(f'[{e.__class__.__name__}]: {e.args}')
