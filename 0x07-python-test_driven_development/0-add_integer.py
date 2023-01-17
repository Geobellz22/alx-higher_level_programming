#!/usr/bin/python3
"""Function adds integers"""


def add_integer(a, b=98):
    """add 2 integers
    Args:
        a (int): integer 3
        b (int): integer 4
    Returns:
        a + b as int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
