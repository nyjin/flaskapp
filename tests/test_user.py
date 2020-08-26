from flaskapp.schemas import UserSchema
from flaskapp.models import User
from pprint import pprint


def test_dump():
    user = User(first_name="first", middle_name="middle", last_name="last")
    result = UserSchema().dump(user)
    assert result["name"] != None
