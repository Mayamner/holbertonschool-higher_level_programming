#!/usr/bin/env python3
"""Module for serializing and deserializing custom objects using pickle."""
import pickle


class CustomObject:
    """Represents a custom object with name, age, and student status."""

    def __init__(self, name, age, is_student):
        """Initialize a new CustomObject."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in a readable format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance and save it to filename."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return a CustomObject instance from filename."""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
