from typing import List

import json
from .extensions import db
from . import models, schemas

from flask_restful import Resource, reqparse, Api
from flask import Blueprint, request

api_blueprint = Blueprint("api", __name__)
api = Api(api_blueprint)


# class UserList(Resource):
#     def get(self):
#         users = db.session.query(models.User).all()
#         return schemas.users_schema.dump(users)


class HobbyList(Resource):
    def get(self):
        hobbies = db.session.query(models.Hobby).all()
        return schemas.hobbies_schema.dump(hobbies)

    def post(self):
        session = db.session
        with session.begin_nested():
            hobby = schemas.hobby_schema.load(request.json)
            session.add(hobby)

        return schemas.hobby_schema.dump(hobby), 201


class HobbyById(Resource):
    def get(self, id: int):
        hobby = db.session.query(models.Hobby).filter(models.Hobby.id == id).first()
        return schemas.hobby_schema.dump(hobby), 200

    def put(self, id: int):
        session = db.session
        with session.begin_nested():
            hobby = session.query(models.Hobby).filter(models.Hobby.id == id).first()
            schemas.hobby_schema.load(request.json, instance=hobby, partial=True)

        return schemas.hobby_schema.dump(hobby), 200


# api.add_resource(UserList, "/users")
api.add_resource(HobbyList, "/hobbies")
api.add_resource(HobbyById, "/hobbies/<int:id>")
