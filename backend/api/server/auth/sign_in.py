#!/usr/bin/python3
"""Index"""
from flask import request, jsonify
from api.server.auth import app_auth
from models.user import User
from models import storage

@app_auth.route('/sign_in/', methods=['POST'], strict_slashes=False)
def sign_in():
    """Sign In Page Auth"""
    from api.app import bcrypt

    if not request.is_json:
        return jsonify(message="Request is not a JSON"), 415

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email:
        return jsonify(message="Email is required"), 400
    elif not password:
        return jsonify(message="Password is required"), 400
    
    existing_user = storage.get_by_email(User, email)
    hashed_pass = bcrypt.check_password_hash(existing_user.password, password)

    if not existing_user or not hashed_pass:
        return jsonify(message="Invalid email or password"), 401

    user_data = { "id": existing_user.id, "email": existing_user.email, "first_name": existing_user.first_name, "last_name": existing_user.last_name }

    return jsonify(message="User sign in successful", user=user_data), 200
