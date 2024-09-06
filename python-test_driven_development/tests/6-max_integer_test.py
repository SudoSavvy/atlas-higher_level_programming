#!/usr/bin/python3
"""
This module contains the max_integer function.
"""

def max_integer(lst=[]):
    """
    Function to find the maximum integer in a list of integers.

    Args:
        lst (list): List of integers. Default is an empty list.

    Returns:
        int: The maximum integer from the list. If the list is empty, returns None.

    Raises:
        TypeError: If the list contains non-integer values.
    """
    if not all(isinstance(i, int) for i in lst):
        raise TypeError("list must contain only integers")

    if len(lst) == 0:
        return None

    max_int = lst[0]
    for num in lst:  # Complete the for loop here
        if num > max_int:
            max_int = num

    return max_int
