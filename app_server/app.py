#!/usr/bin/env python
from flask import Flask
from db import main_storage
from json import load

app = Flask(__name__)


@app.teardown_appcontext
def close_session():
    main_storage.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
