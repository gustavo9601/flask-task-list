from flask import Blueprint

# Blueprint('nombre del bluprint', name_file, url_prefix='/prefijo de ruta')
auth = Blueprint('auth', __name__, url_prefix='/auth')

from . import views

