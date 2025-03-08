import pytest
from db import Database

@pytest.fixture
def db():
    """Provide a new instance of the database class and cleans up after the test."""
    database = Database()
    yield database # Provide the fixture instance
    database.data.clear() # Cleanup step (not needed for in-memory, but useful for real Dbs)
    
def test_add_user(db):
    db.add_user(1, "Ade")
    assert db.get_user(1) == "Ade"
    
def test_add_duplicate_user(db):
    db.add_user(1, "Ade")
    with pytest.raises(ValueError, match="User already exisits"):
        db.add_user(1, "Joe")
        
def test_delete_user(db):
    db.add_user(2, "Joe")
    db.delete_user(2)
    assert db.get_user(2) is None