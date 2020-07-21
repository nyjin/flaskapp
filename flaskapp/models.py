import re
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


class User(ModelMixins, db.Model):
    name = db.Column(db.String(64), index=True, nullable=False)
    email = db.Column(db.String(128), unique=True, index=True, nullable=False)
    todos = db.relationship("todo", backref=db.backref("user"))
    hobby = db.relationship("hobby", backref=db.backref("user", uselist=False))


class Hobby(ModelMixins, db.Model):
    name = db.Column(db.String(64), index=True, nullable=False)


class Todo(ModelMixins, db.Model):
    name = db.Column(db.String(64), index=True, nullable=False)
