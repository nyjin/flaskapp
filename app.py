from flaskapp.main import create_app
from flask_script import Manager
from flaskapp.extensions import db

app = create_app()
manager = Manager(app)


@manager.command
def createdb():
    with app.app_context():
        db.create_all()
        db.session.commit()


if __name__ == "__main__":
    manager.run()
