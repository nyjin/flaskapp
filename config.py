import os


class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///sample.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.environ.get("SECRET_KEY") or "jfuUYH7472JUjlkjqmlluiNMh18n"
    BOOTSTRAP_SERVE_LOCAL = True
    FLASK_DEBUG = True
    DEBUG = True
