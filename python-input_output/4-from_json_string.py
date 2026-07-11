#!/usr/bin/python3
"""Module that returns an object from a JSON string representation."""
import json


def from_json_string(my_str):
    """Return an object represented by a JSON string."""
    return json.loads(my_str)
