#!/usr/bin/python3
"""Module that returns the dict description of a simple object for JSON."""


def class_to_json(obj):
    """Return the dictionary description of a simple-structure object."""
    return obj.__dict__
