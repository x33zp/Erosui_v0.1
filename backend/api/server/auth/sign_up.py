#!/usr/bin/python3
"""Index"""
from flask import request, jsonify
from api.server.auth import app_auth
from models.user import User
from models import storage

@app_auth.route('/sign_up/', methods=['POST'], strict_slashes=False)
def login():
    """Sign Up Page Auth"""
    from api.app import bcrypt

    if not request.is_json:
        return jsonify(message="Request is not a JSON"), 415

    data = request.get_json()
    
    email = data.get("email")
    firstName = data.get("first_name")
    lastName = data.get("last_name")
    password = data.get("password")
    pass_cfm = data.get("pass_cfm")

    if not email:
        return jsonify(message="Email is required"), 400
    elif not firstName:
        return jsonify(message="First name is required"), 400
    elif not lastName:
        return jsonify(message="Last name is required"), 400
    elif not password or len(password) < 8:
        return jsonify(message="Password can\'t be lass than 8 characters"), 400
    elif password != pass_cfm:
        return jsonify(message="Passwords don\'t match"), 400

    existing_user = storage.get_by_email(User, email)

    if existing_user:
        return jsonify(message="User already exists"), 409
    
    hashed_pass = bcrypt.generate_password_hash(password).decode('utf-8')

    new_user = User(email=email, first_name=firstName, last_name=lastName, password=hashed_pass)
    new_user.save()

    del data["password"]
    del data["pass_cfm"]

    return jsonify(message="User created successfully", user=data), 201
