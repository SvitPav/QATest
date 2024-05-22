class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Sergii"
        self.second_name = "Butenko"

    def remove(self):
        self.name = ""
        self.second_name = ""


def test_remove_name(user):
    user.name = ""
    assert user.name == ""

def test_name(user):
    assert user.name == "Sergii"

def test_second_name(user):
    assert user.second_name == "Butenko"


