import pytest

@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()

