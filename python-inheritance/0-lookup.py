#!/usr/bin/python3
"""
This module provides a function to return the list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object whose attributes and methods need to be returned.

    Returns:
        A list containing the available attributes and methods of the object.
    """
    return dir(obj)
