#!/usr/bin/python3
"""
This module contains the function `add_integer` which adds two integers or floats.
"""

def add_integer(a, b=98):
    """Adds two integers or floats."""
    # Check if a is a float and if it is NaN or too large
    if isinstance(a, float):
        if a != a or a == float('inf') or a == -float('inf'):
            raise TypeError("a must be an integer")
    
    # Check if b is a float and if it is NaN or too large
    if isinstance(b, float):
        if b != b or b == float('inf') or b == -float('inf'):
            raise TypeError("b must be an integer")

    # Ensure both a and b are integers
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Cast floats to integers
    a = int(a)
    b = int(b)
    
    return a + b
