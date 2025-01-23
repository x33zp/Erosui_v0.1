#!/usr/bin/python3
"""Index"""
from flask import request, jsonify
from api.server.protected import authed
from models.user import User
from models import storage
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


@authed.route('/profile/', methods=['GET'], strict_slashes=False)
@jwt_required()
def user_profile():
    """Return user profile details"""
    #try:
     #   current_user = get_jwt_identity()
      #  c_userData = storage.get_by_email(User, current_user)

    response_body = {
        "email": get_jwt_identity(),
        "about": "Hello! I'm a full stack developer that loves python and javascript"
    }
    return jsonify(response_body), 200

    #except Exception as e:
        #return jsonify({"error": str(e)}), 500
