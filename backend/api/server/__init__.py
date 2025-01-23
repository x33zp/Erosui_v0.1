#!/usr/bin/python3
"""Init"""
from flask import Blueprint

auth = Blueprint('auth', __name__)

from .auth import *
