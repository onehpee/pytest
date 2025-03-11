from main import get_food, add, divide, User, is_prime
import pytest

def test_get_food():
    assert get_food(55) == "rice"
    
    
def test_add():
    assert add(9, 1) == 10, "9 + 1 should be 10"
    assert add(-6, 4) == -2, "-6 + 4 should be -2"
    assert add(0, 0) == 0, "0 + 0 should be 0"
    
    
def test_divide():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(4, 0)
        
        
@pytest.fixture
def user():
    """Creates a freash instance of User before each test."""
    return user()

def test_add_user(user):
    assert user.add_user("john_doe", "john@example.com") == True
    assert user.add_user("john_doe") == "john@example.com"
    
    
def test_add_duplicate_user(user):
    user.add_user("john_doe", "john@example.com")
    with pytest.raises(ValueError):
        user.add_user("john_doe", "john@example.com")
    
@pytest.mark.parametrize("num, expected", [
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (17, True),
    (18, False),
    (19, True),
    (25, False),
])
def test_is_prime(num ,expected):
    assert is_prime(num) == expected
    