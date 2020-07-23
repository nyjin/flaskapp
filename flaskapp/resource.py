from flask_restful import Resource

from flask import Blueprint
from .extensions import db
from .models import Hobby
from flask_restful import Api

api_blueprint = Blueprint("api", __name__)
api = Api(api_blueprint)


class UserList(Resource):
    def get(self):
        return "Hello world"

class HobbyList(Resource):
    def get(self):
        return "Hello world2"

class HobbyById(Resource):
    def get(self, id):
        return db.session.query(Hobby).get(id)


api.add_resource(UserList, "/users")
api.add_resource(HobbyList, "/hobby")
api.add_resource(HobbyById, "/hobby/<int:id>")
