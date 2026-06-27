#!/usr/bin/python3
"""Module that defines inherits_from function."""


def inherits_from(obj, a_class):
    """Returns True only if obj is an instance of a class that inherited
    from a_class (not an exact match)."""
    return isinstance(obj, a_class) and type(obj) is not a_class
