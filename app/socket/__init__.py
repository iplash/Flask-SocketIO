from flask import Blueprint

socket = Blueprint('socket', __name__)

from . import routes, events