#!/usr/bin/python3
"""
This module provides the `class_to_json` function.
"""

def class_to_json(obj):
    """
    Returns the dictionary description with simple data structures
    (list, dictionary, string, integer, and boolean) for JSON serialization of an object.

    Args:
        obj (object): An instance of a class.

    Returns:
        dict: The dictionary representation of the object's attributes.
    """
    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
    return {}
