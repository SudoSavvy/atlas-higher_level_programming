#!/usr/bin/python3
"""
This module defines the function `print_square`.

The function prints a square made of the character `#` based on the given size.

Raises:
    TypeError: If `size` is not an integer.
    ValueError: If `size` is less than 0.
"""

def print_square(size):
    """Prints a square with the character `#`.

    Args:
        size (int): The length of the square's sides.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square if size is valid
    for _ in range(size):
        print("#" * size)
