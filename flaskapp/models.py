import re
from sqlalchemy.orm import backref
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from flaskapp.extensions import db

_camel_to_snake = re.compile(r"(?<!^)(?=[A-Z])")


class ModelMixins(object):
    @declared_attr
    def __tablename__(cls):
        return _camel_to_snake.sub("_", cls.__name__).lower()

    __table_args__ = {"mysql_engine": "InnoDB"}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    created_by = db.Column(db.String(64), default="SYSTEM", nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    updated_by = db.Column(db.String(64), default="SYSTEM", nullable=False)


class AuthGroup(ModelMixins, db.Model):
    name = db.Column(db.String(64), index=True, nullable=False)
    users = db.relationship("User", secondary="auth_group_map")

class AuthGroupMap(ModelMixins, db.Model):
    auth_group_id = db.Column(db.Integer, db.ForeignKey('auth_group.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    auth_group = db.relationship("AuthGroup", backref=backref("auth_group_map", cascade="all, delete-orphan" ))
    user = db.relationship("User", backref=backref("auth_group_map", cascade="all, delete-orphan" ))


class User(ModelMixins, db.Model):
    name = db.Column(db.String(64), index=True, nullable=False)
    email = db.Column(db.String(128), unique=True, index=True, nullable=False)
    
    hobby_id = db.Column(
        db.ForeignKey("hobby.id"),
        nullable=False,
        index=True,
        info="취미",
    )

    hobby = db.relationship("Hobby", primaryjoin="user.hobby_id == hobby.id",
        backref=backref("User", uselist=False))
    
    todo_id = db.Column(
        db.ForeignKey("todo.id"),
        nullable=False,
        index=True,
        info="할일",
    )

    todos = db.relationship("Todo", primaryjoin="user.todo_id == todo.id",
        backref=backref("User"))
    
    auth_groups = db.relationship("AuthGroup", secondary="auth_group_map")


class Hobby(ModelMixins, db.Model):
    name = db.Column(db.String(64), index=True, nullable=False)


class Todo(ModelMixins, db.Model):
    name = db.Column(db.String(64), index=True, nullable=False)
