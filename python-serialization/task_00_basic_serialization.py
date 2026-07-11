#!/usr/bin/env python3
"""Module for basic serialization and deserialization of data using JSON."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary and save it to a JSON file.

    Args:
        data (dict): The data to serialize.
        filename (str): The output JSON file. Replaced if it exists.
    """
    with open(filename, "w", encoding="utf8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize JSON data from a file.

    Args:
        filename (str): The input JSON file.

    Returns:
        dict: The deserialized data.
    """
    with open(filename, encoding="utf8") as f:
        return json.load(f)
