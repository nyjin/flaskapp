import re
from sqlalchemy.orm import backref
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from flaskapp.extensions import db

_camel_to_snake = re.compile(r"(?<!^)(?=[A-Z])")


class ModelMixins(object):
    @declared_attr
    def __tablename__(cls):
        return _camel_to_snake.sub("_", cls.__name__).lower()

    __table_args__ = {"mysql_engine": "InnoDB", "extend_existing": True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    created_by = db.Column(db.String(64), default="SYSTEM", nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False)
    updated_by = db.Column(db.String(64), default="SYSTEM", nullable=False)


class AuthGroup(ModelMixins, db.Model):
    name = db.Column(db.String(64), index=True, nullable=False)
    users = db.relationship("User", secondary="auth_group_map")

class User(ModelMixins, db.Model):
    name = db.Column(db.String(64), index=True, nullable=False)
    email = db.Column(db.String(128), unique=True, index=True, nullable=False)
    
    hobby_id = db.Column(
        db.ForeignKey("hobby.id"),
        nullable=True,
        index=True,
        info="취미",
    )


    hobby = db.relationship("Hobby",
        foreign_keys=hobby_id,
        backref=backref("user"),
        uselist=False)

    todos = db.relationship("Todo",
        lazy=False,
        uselist=True
        )
    
    auth_groups = db.relationship("AuthGroup", secondary="auth_group_map")


class AuthGroupMap(ModelMixins, db.Model):
    auth_group_id = db.Column(db.Integer, db.ForeignKey('auth_group.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    auth_group = db.relationship("AuthGroup", 
        primaryjoin=auth_group_id == AuthGroup.id,
        backref=backref("auth_group_map", cascade="all, delete-orphan"))
    user = db.relationship("User", 
        primaryjoin=user_id == User.id,
        backref=backref("auth_group_map", cascade="all, delete-orphan"))

class Hobby(ModelMixins, db.Model):
    name = db.Column(db.String(64), index=True, nullable=False)


class Todo(ModelMixins, db.Model):
    name = db.Column(db.String(64), index=True, nullable=False)

    user_id = db.Column(db.Integer, 
        db.ForeignKey('user.id'),
        nullable=False,
        index=True)

    user = db.relationship("User", 
        primaryjoin=user_id == User.id)
