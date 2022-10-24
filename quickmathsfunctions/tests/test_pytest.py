from quickmathsfunctions.src.quickmathsfunctions import add, divide, multiply, subtract


def test_add():
    assert add(10, 5) == 15

def test_subtract():
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(10, 10) == 100

def test_divide():
    assert divide(5, 10) == 0.5

