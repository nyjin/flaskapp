from flaskapp.models import *
from flask_sqlalchemy import SQLAlchemy, SessionBase


class TestData:
    def __init__(self, session: SessionBase):
        self._session = session

        self._roh = User(name="Roh", email="z1@naver.com")
        self._park = User(name="Park", email="z2@naver.com")

        self._users = [self._roh, self._park]

    def _add_users_with_hobbies(self):
        h1 = Hobby(name="watch TV")
        h2 = Hobby(name="reading books")
        h3 = Hobby(name="swimming")
        h4 = Hobby(name="dance")

        self._roh.hobby = h1
        self._park.hobby = h4

        self._session.add_all([h1, h2, h3, h4])

    def _add_users_with_todos(self):
        todo1 = Todo(name="goto school")
        todo2 = Todo(name="get the work")
        todo3 = Todo(name="write coding")
        todo4 = Todo(name="have a fun stuff")

        self._roh.todos.append(todo1)
        self._park.todos.append(todo2)
        self._park.todos.append(todo3)
        self._park.todos.append(todo4)

        self._session.add_all([todo1, todo2, todo3, todo4])

    def _add_users_with_groups(self):
        g1 = AuthGroup(name="manager")
        g2 = AuthGroup(name="employee")

        m1 = AuthGroupMap(auth_group=g1, user=self._roh, used=True)
        m2 = AuthGroupMap(auth_group=g2, user=self._park, used=False)

        self._session.add_all([g1, g2])
        self._session.add_all([m1, m2])

    def add_users(self):

        self._add_users_with_hobbies()
        self._add_users_with_todos()
        self._add_users_with_groups()
        self._session.add_all(self._users)


def add_test_data(db: SQLAlchemy):

    session = db.session
    with session.begin_nested():
        test_data = TestData(session)
        test_data.add_users()

