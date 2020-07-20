from flask_restful import Resource

from flask import Blueprint
from flask_restful import Api

api_blueprint = Blueprint("api", __name__)
api = Api(api_blueprint)


class UserList(Resource):
    def get(self):
        return "Hello world"


api.add_resource(UserList, "/users")
