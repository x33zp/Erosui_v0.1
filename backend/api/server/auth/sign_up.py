#!/usr/bin/python3
"""Index"""
from flask import request, abort
from api.server import app_auth
from models.user import User


@app_auth.route('/sign_up/', methods=['GET', 'POST'], strict_slashes=False)
def login():
    """Sign Up Page Auth"""
    # return "Sign UP Page"

    if not request.is_json:
        abort(400, description="Not a JSON")

    data = request.get_json()
    print('DATA {}'.format(data))

    if 'name' not in data:
        abort(400, description="Missing name")

    new_user = User(**data)
    new_user.save()

    return {"message": "User created successfully", "user": data}, 201
