#!/usr/bin/env python3
"""Module that defines Shape ABC, Circle, Rectangle, and shape_info."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Abstract method for area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method for perimeter."""
        pass


class Circle(Shape):
    """A Circle that inherits from Shape."""

    def __init__(self, radius):
        """Initializes Circle with a radius."""
        self.radius = radius

    def area(self):
        """Returns the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Returns the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """A Rectangle that inherits from Shape."""

    def __init__(self, width, height):
        """Initializes Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints the area and perimeter of a shape using duck typing."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
