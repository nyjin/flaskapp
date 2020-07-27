from marshmallow import pre_load, post_load, pre_dump, post_dump
from marshmallow_sqlalchemy import auto_field, field_for
from stringcase import camelcase, snakecase
from .extensions import ma
from . import models


class CodecMixin:
    @pre_load
    def to_snakecase(self, data, **kwargs):
        return {snakecase(key): value for key, value in data.items()}

    @post_load
    def load_into_object(self, data, many, partial):
        if self.instance:
            for key, value in data.items():
                setattr(self.instance, key, value)
            return self.instance
        else:
            return self.Meta.model(**data)

    @post_dump
    def to_camelcase(self, data, **kwargs):
        return {camelcase(key): value for key, value in data.items()}


class HobbySchema(ma.SQLAlchemySchema, CodecMixin):
    id = field_for(models.Hobby, "id", required=True, dump_only=True)
    name = field_for(models.Hobby, "name", required=True)

    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)

    class Meta:
        model = models.Hobby
        strict = (True,)
        fields = ("id", "name", "created_at", "updated_at")
        ordered = True


# class UserSchema(TimeSchemaMixin):
#     id = field_for(models.Hobby, "id", required=True)
#     name = field_for(models.User, "name", required=True)
#     hobby = ma.Nested(HobbySchema, many=True)
#     authGroup = ma.Nested(AuthGroupSchema, many=True)

#     class Meta:
#         model = models.User


hobby_schema = HobbySchema()
hobbies_schema = HobbySchema(many=True)
# users_schema = UserSchema(many=True)
