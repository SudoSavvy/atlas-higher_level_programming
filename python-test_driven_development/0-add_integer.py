#!/usr/bin/python3
"""
This module contains the function `add_integer` which adds two integers or floats.
"""

def add_integer(a, b=98):
    """
    Returns the sum of two integers or floats.
    Both arguments are first cast to integers if they are float types.
    
    Arguments:
    a -- the first number to add (must be an integer or float)
    b -- the second number to add (default: 98, must be an integer or float)
    
    Raises:
    TypeError if either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Cast both to integers (if they are floats)
    return int(a) + int(b)
