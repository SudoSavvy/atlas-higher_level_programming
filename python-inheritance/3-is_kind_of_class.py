#!/usr/bin/python3
"""
Module to define a function that checks if an object is an instance of,
or if it is an instance of a class that inherited from, the specified class.

Function:
- is_kind_of_class: Returns True if obj is an instance of a_class or
  if obj is an instance of a class that inherited from a_class;
  otherwise False.
"""

def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or if obj is an instance
    of a class that inherited from a_class; otherwise False.

    Parameters:
    obj: The object to check.
    a_class: The class to compare against.

    Returns:
    bool: True if obj is an instance of a_class or if obj is an instance
          of a class that inherited from a_class; otherwise False.
    """
    return isinstance(obj, a_class)
