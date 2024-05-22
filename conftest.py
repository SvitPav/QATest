import pytest
from user import User

@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()
