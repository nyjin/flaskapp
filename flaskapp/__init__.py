from flask import Blueprint
from flask_restful import Api
from .models import *

api_blueprint = Blueprint("api", __name__)
api = Api(api_blueprint)
