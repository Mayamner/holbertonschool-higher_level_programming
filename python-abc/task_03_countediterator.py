#!/usr/bin/env python3
"""Module that defines CountedIterator class."""


class CountedIterator:
    """An iterator that counts how many items have been fetched."""

    def __init__(self, iterable):
        """Initializes with an iterable and a counter at 0."""
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Returns the current count of items iterated."""
        return self.count

    def __next__(self):
        """Fetches next item and increments counter."""
        item = next(self.iterator)
        self.count += 1
        return item
