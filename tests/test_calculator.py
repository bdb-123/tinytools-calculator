from src.calculator import add

def test_add():
    assert add(2, 3) == 5

from src.calculator import subtract

def test_subtract():
    assert subtract(5, 2) == 3

from src.calculator import multiply

def test_multiply():
    assert multiply(4, 3) == 12

