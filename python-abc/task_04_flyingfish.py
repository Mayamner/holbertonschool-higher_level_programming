#!/usr/bin/env python3
"""Module for FlyingFish multiple inheritance task."""


class Fish:
    """A class representing a fish."""

    def swim(self):
        """Print swimming message."""
        print("The fish is swimming")

    def habitat(self):
        """Print fish habitat."""
        print("The fish lives in water")


class Bird:
    """A class representing a bird."""

    def fly(self):
        """Print flying message."""
        print("The bird is flying")

    def habitat(self):
        """Print bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A class representing a flying fish (multiple inheritance)."""

    def fly(self):
        """Override fly to print flying fish message."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override swim to print flying fish message."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override habitat to print flying fish message."""
        print("The flying fish lives both in water and the sky!")
