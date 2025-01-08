#!/usr/bin/python3
"""Index"""
from api.server import app_auth


@app_auth.route('/sign_in/', methods=['GET', 'POST'], strict_slashes=False)
def sign_in():
    """Sign In  Page Auth"""
    return "Sign In Page"
