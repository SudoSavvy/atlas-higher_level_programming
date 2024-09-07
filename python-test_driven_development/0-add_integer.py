#!/usr/bin/python3
"""
Module to add two integers
"""

def add_integer(a, b=98):
    """Function to add two integers or floats

    Args:
        a: First number (must be an integer or a float)
        b: Second number (default is 98, must be an integer or a float)

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b are not integers or floats.
        ValueError: If a or b are NaN (not a number).
    """
    # Check if 'a' is a float or integer
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    # Check if 'b' is a float or integer
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Check for NaN (Not a Number) for 'a'
    if a != a:
        raise ValueError("cannot convert float NaN to integer")
    # Check for NaN (Not a Number) for 'b'
    if b != b:
        raise ValueError("cannot convert float NaN to integer")

    # Cast floats to integers
    a = int(a)
    b = int(b)

    return a + b
