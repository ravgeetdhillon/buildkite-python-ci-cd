def add(a, b):
    """
    >>> add(5, 10)
    15
    """

    return a + b


def subtract(a, b):
    """
    >>> subtract(5, 10)
    -5
    """

    return a - b


def multiply(a, b):
    """
    >>> multiply(5, 10)
    50
    """

    return a * b


def divide(a, b):
    """
    >>> divide(5, 10)
    0.5
    """

    return a / b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
