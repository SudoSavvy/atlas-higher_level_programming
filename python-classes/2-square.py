#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute.
The class includes validation to ensure size is an integer and >= 0.
"""


class Square:
    """
    A class that defines a square with a private size attribute.
    """

    def __init__(self, size=0):
        """
        Initialize the square with a given size, which must be an integer.
        Raise a TypeError if size is not an integer.
        Raise a ValueError if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
