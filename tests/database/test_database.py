import pytest
from modules.common.database.py import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()
