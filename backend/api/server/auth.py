#!/usr/bin/python3
"""Index"""
from flask import request, jsonify
import json
from api.server import auth
from models.user import User
from models import storage
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity, get_jwt
from datetime import datetime, timedelta, timezone
from api.services.auth_service import hash_password, check_hashed_password, generate_access_token


@auth.route('/register/', methods=['POST'], strict_slashes=False)
def register():
    """Endpoint to register a new user."""
    #from api.app import bcrypt

    if not request.is_json:
        return jsonify(message="Request is not a JSON"), 415

    data = request.get_json()
    
    email = data.get("email", None)
    firstName = data.get("first_name", None)
    lastName = data.get("last_name", None)
    password = data.get("password", None)
    pass_cfm = data.get("pass_cfm", None)

    if firstName is None or firstName == '':
        return jsonify(message="First name is required"), 400
    elif lastName is None or lastName == '':
        return jsonify(message="Last name is required"), 400
    elif email is None or email == '':
        return jsonify(message="Email is required"), 400
    elif password is None or len(password) < 8 or password == '':
        return jsonify(message="Password can\'t be lass than 8 characters"), 400
    elif password != pass_cfm:
        return jsonify(message="Passwords don\'t match"), 400

    existing_user = storage.get_by_email(User, email)

    if existing_user:
        return jsonify(message="User already exists"), 409
    
    hashed_password = hash_password(password)

    new_user = User(email=email, first_name=firstName, last_name=lastName, password=hashed_password)
    new_user.save()

    del data["password"]
    del data["pass_cfm"]

    return jsonify(message="User created successfully", user=data), 201


@auth.route('/login/', methods=['POST'], strict_slashes=False)
def login():
    """Endpoint to log in a user."""
    #from api.app import bcrypt

    if not request.is_json:
        return jsonify(message="Request is not a JSON"), 415

    data = request.get_json()

    email = data.get("email", None)
    password = data.get("password", None)

    if email is None:
        return jsonify(message="Email is required"), 400
    elif password is None:
        return jsonify(message="Password is required"), 400

    existing_user = storage.get_by_email(User, email)

    if not existing_user:
        return jsonify(message="Invalid email or password"), 401
    elif not check_hashed_password(existing_user.password, password):
        return jsonify(message="Invalid email or password"), 401

    access_token = create_access_token(identity=email)
    user_data = { "id": existing_user.id, "email": existing_user.email, "first_name": existing_user.first_name, "last_name": existing_user.last_name }

    return jsonify(message="User sign in successful", access_token=access_token, user=user_data), 200

@auth.after_request
def refreshing_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = generate_access_token(identity=get_jwt_identity())
            if response.is_json:
                data = response.get_json()
                data["access_token"] = access_token
                response.data = json.dumps(data)
        return response
    except (RuntimeError, KeyError):
        return response
