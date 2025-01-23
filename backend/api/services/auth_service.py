#!/usr/bin/python3
"""Authentication Services"""
#from api.app import bcrypt
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity, get_jwt
from datetime import datetime, timedelta, timezone
import json


def hash_password(password):
    """Hash a plain text password."""
    from api.app import bcrypt

    return bcrypt.generate_password_hash(password).decode('utf-8')

def check_hashed_password(hashed, plain):
    """Check if the provided password matches the hashed password."""
    from api.app import bcrypt

    return bcrypt.check_password_hash(hashed, plain)

def generate_access_token(identity):
    """
    Generate a JWT access token.
    :param identity: User identifier (e.g., user ID or email)
    """
    return create_access_token(identity=identity)
