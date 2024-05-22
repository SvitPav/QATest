import pytest


class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = 'Sergii'
        self.second_name = 'Butenko'

    def remove(self):
        self.name = ''
        self.second_name = ''


@pytest.fixture
def user():
    user = User()
    user.create()
    
    yield user
    
    user.remove()


    user.create()

    assert user.name == 'Sergii'
    user.remove()

    user.create()

    assert user.second_name == 'Butenko'
    user.remove()

    

    


