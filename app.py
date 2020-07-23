from flaskapp.main import create_app
from flask_script import Manager, prompt_bool
from flaskapp.extensions import db
from testdata import add_test_data
from flaskapp.models import *

app = create_app()
manager = Manager(app)


@manager.command
def createdb():
    session = db.session
    db.drop_all()
    db.create_all()
    h1 = Hobby(name="watch TV")
    h2 = Hobby(name="readint books")
    h3 = Hobby(name="swimming")
    h4 = Hobby(name="dance")

    todo1 = Todo(name="goto school")
    todo2 = Todo(name="get the work")
    todo3 = Todo(name="write coding")
    todo4 = Todo(name="have a fun stuff")

    # roh = User(name="Roh", todos=[todo1], hobby=h1)
    # park = User(name="Park", todos=[todo2,todo3,todo4], hobby=h4)
    roh = User(name="Roh", hobby=h1, email='z1@naver.com')
    park = User(name="Park", hobby=h4, email='z2@naver.com')

    g1 = AuthGroup(name="manager", users=[roh])
    g2 = AuthGroup(name="employee", users=[park])

    roh.todos.append(todo1)
    park.todos.append(todo2)
    park.todos.append(todo3)
    park.todos.append(todo4)

    session.add_all([g1,g2])
    session.add_all([h1,h2,h3,h4])
    session.add_all([roh,park])

    session.commit()
    # add_test_data(session = db.session)

if __name__ == "__main__":
    manager.run()
