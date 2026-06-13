#!/usr/bin/python3
"""Module for adding integers."""


def add_integer(a, b=98):
    """Adds 2 integers.

    Args:
        a: first integer
        b: second integer (default 98)

    Returns:
        The addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
