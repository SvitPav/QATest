import pytest


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


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


import pytest
from modules import GitHubAPI  # Припустимо, що у вас є модуль, який містить клас GitHubAPI

@pytest.fixture
def github_api():
    # Ініціалізуємо екземпляр класу GitHubAPI або будь-який інший код, який потрібний для підготовки до використання GitHub API
    api = GitHubAPI()
    return api

def test_github_api_call(github_api):
    # Тест, який використовує фікстуру github_api для виклику GitHub API
    response = github_api.call_some_method()
    assert response.status_code == 200

@pytest.fixture
def github_api():
    # Ініціалізуємо екземпляр класу GitHubAPI або будь-який інший код, який потрібний для підготовки до використання GitHub API
    api = GitHubAPI()
    return api

def test_github_api_call(github_api):
    # Тест, який використовує фікстуру github_api для виклику GitHub API
    response = github_api.call_some_method()
    assert response.status_code == 200
