#!/usr/bin/python3
"""
This module contains the max_integer function.
"""

def max_integer(lst):
    """
    Function to find the maximum integer or float in a list.

    Args:
        lst (list): List of integers or floats.

    Returns:
        int or float: The maximum value in the list. If the list is empty, returns None.

    Raises:
        TypeError: If the list contains non-numeric values.
    """
    if not all(isinstance(x, (int, float)) for x in lst):
        raise TypeError("List must contain only integers or floats")

    if len(lst) == 0:
        return None

    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num

    return max_val
