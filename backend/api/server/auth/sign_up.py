#!/usr/bin/python3
"""Index"""
from api.server import app_auth


@app_auth.route('/sign_up/', strict_slashes=False)
def login():
    """Sign Up Page Auth"""
    return "Sign Up"
