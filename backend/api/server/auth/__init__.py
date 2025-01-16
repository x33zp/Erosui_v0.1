#!/usr/bin/python3
"""Init"""
from flask import Blueprint

app_auth = Blueprint('access', __name__)

from .sign_in import *
from .sign_up import *
