#!/usr/bin/python3
"""
Module to define a function that checks if an object is exactly an instance
of a specified class.

Function:
- is_same_class: Returns True if obj is exactly an instance of a_class;
  otherwise False.
"""

def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class; otherwise False.

    Parameters:
    obj: The object to check.
    a_class: The class to compare against.

    Returns:
    bool: True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
