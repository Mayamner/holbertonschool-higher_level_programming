#!/usr/bin/env python3
"""Module that defines Animal ABC with Dog and Cat subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses."""
        pass


class Dog(Animal):
    """A Dog that inherits from Animal."""

    def sound(self):
        """Returns the sound a dog makes."""
        return "Bark"


class Cat(Animal):
    """A Cat that inherits from Animal."""

    def sound(self):
        """Returns the sound a cat makes."""
        return "Meow"
