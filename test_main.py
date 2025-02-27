from main import get_food, add, divide
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
    