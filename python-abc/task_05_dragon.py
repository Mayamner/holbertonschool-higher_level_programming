#!/usr/bin/env python3
"""Module for Dragon mixin task."""


class SwimMixin:
    """Mixin that provides swimming ability."""

    def swim(self):
        """Print swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying ability."""

    def fly(self):
        """Print flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon that can swim, fly, and roar."""

    def roar(self):
        """Print roaring message."""
        print("The dragon roars!")