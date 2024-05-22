import pytest


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()

def test_change_name(user):
    assert user.name == 'Sergii'

def test_change_second_name(user):
    assert user.second_name == 'Butenko'
