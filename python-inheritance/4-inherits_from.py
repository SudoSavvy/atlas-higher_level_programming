#!/usr/bin/python3
"""
Module to define a function that checks if an object is an instance of
a class that inherited (directly or indirectly) from the specified class.

Function:
- inherits_from: Returns True if obj is an instance of a class that inherited
  from a_class (directly or indirectly); otherwise False.
"""

def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited from a_class
    (directly or indirectly); otherwise False.

    Parameters:
    obj: The object to check.
    a_class: The class to compare against.

    Returns:
    bool: True if obj is an instance of a class that inherited from a_class,
          otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
