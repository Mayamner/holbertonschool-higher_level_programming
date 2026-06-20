#!/usr/bin/python3
"""This module defines a Square class, based on Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class defines a square, inherited from Rectangle."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        super().__init__(size, size)

    def __str__(self):
        """Return the printable representation of the square."""
        return "[Square] {}/{}".format(self.width, self.height)

    @property
    def size(self):
        """Get/set the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set size by reusing the width setter's validation."""
        self.width = value
        self.height = value
