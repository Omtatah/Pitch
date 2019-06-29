from flask import Blueprint

from . import views, errors

#Initializing main sub-folder ->
main = Blueprint('main', __name__)
