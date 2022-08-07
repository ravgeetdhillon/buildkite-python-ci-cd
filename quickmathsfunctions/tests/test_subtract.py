from quickmathsfunctions.src.quickmathsfunctions import subtract


def test_positive_subtract():
    assert subtract(10, 5) == 5


def test_self_subtract():
    assert subtract(10, 10) == 0


def test_negative_subtract():
    assert subtract(5, 10) == -5

