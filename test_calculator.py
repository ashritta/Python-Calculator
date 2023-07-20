from calculator import *

def test_add():
    assert add(-3, -2) == -5
    assert add(-1, 0) == -1
    assert add(1, 2) == 3
    assert add(3, -4) == -1

def test_subtract():
    assert subtract(-3, -2) == -1
    assert subtract(-1, 0) == -1
    assert subtract(1, 2) == -1
    assert subtract(3, -4) == 7

def test_multiply():
    assert multiply(-3, -2) == 6
    assert multiply(-1, 0) == 0
    assert multiply(-1, 2) == -2
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(-3, -2) == 1.5
    assert divide(-1, 0) == None
    assert divide(1, 3) == 1/3
    assert divide(3, 4) == 0.75
