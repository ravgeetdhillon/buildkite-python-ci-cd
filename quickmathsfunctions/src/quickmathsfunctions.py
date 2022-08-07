import doctest


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    """
    >>> divide(5, 10)
    0.5
    >>> divide(5, 5)
    1.0
    >>> divide(10, 5)
    2.0
    >>> divide(10, 0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero
    """

    return a / b


if __name__ == "__main__":
    doctest.testmod()
