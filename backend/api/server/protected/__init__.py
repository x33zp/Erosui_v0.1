#!/usr/bin/python3
"""Init"""
from flask import Blueprint

authed = Blueprint('protected', __name__)

from .profile import *
