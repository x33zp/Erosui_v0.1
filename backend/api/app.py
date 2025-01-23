#!/usr/bin/python3
"""Flask App"""
import os
from flask import Flask
from models import storage
from api.server import auth
from api.server.protected import authed
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from datetime import datetime, timedelta, timezone

load_dotenv()


app = Flask(__name__)
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(authed, url_prefix='/protected')

app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

jwt = JWTManager(app)
bcrypt = Bcrypt(app)
CORS(app)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', threaded=True, debug=True)
