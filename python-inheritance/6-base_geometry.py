#!/usr/bin/python3
"""Module that defines BaseGeometry class with area method."""


class BaseGeometry:
    """A class for geometry with an unimplemented area method."""

    def area(self):
        """Raises an Exception - area() is not implemented."""
        raise Exception("area() is not implemented")
