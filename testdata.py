from flaskapp.models import *

def add_test_data(session):
    with session.begin_nested():
        h1 = Hobby(name="watch TV")
        h2 = Hobby(name="readint books")
        h3 = Hobby(name="swimming")
        h4 = Hobby(name="dance")

        # todo1 = Todo(name="goto school")
        # todo2 = Todo(name="get the work")
        # todo3 = Todo(name="write coding")
        # todo4 = Todo(name="have a fun stuff")

        # roh = User(name="Roh", todos=[todo1], hobby=h1)
        # park = User(name="Park", todos=[todo2,todo3,todo4], hobby=h4)
        roh = User(name="Roh", hobby=h1)
        park = User(name="Park", hobby=h4)

