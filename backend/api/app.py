#!/usr/bin/python3
"""Flask App"""
from flask import Flask
from models import storage
from api.server import app_auth

app = Flask(__name__)
app.register_blueprint(app_auth)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', threaded=True, debug=True)
