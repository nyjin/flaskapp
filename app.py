from flaskapp.main import create_app
from flask_script import Manager, prompt_bool
from flaskapp.extensions import db
from testdata import add_test_data
from flaskapp.models import *

app = create_app()
manager = Manager(app)


@manager.command
def createdb():
    db.drop_all()
    db.create_all()

    add_test_data(db)


if __name__ == "__main__":
    manager.run()
