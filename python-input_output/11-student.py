#!/usr/bin/python3
"""Module that defines a Student class with JSON save/reload support."""


class Student:
    """Defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of a Student instance.

        If attrs is a list of strings, only those attribute names
        are included. Otherwise, all attributes are included.
        """
        if type(attrs) is list and all(type(x) is str for x in attrs):
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the instance with values from json."""
        for key, value in json.items():
            setattr(self, key, value)
