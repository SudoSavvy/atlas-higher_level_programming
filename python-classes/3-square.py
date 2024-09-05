#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute.
The class includes validation to ensure size is an integer and >= 0,
and provides a method to compute the area of the square.
"""


class Square:
    """
    A class that defines a square with a private size attribute.
    """

    def __init__(self, size=0):
        """
        Initialize the square with a given size.
        Raise a TypeError if size is not an integer.
        Raise a ValueError if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size  # Private attribute for size

    def area(self):
        """
        Calculate and return the area of the square.
        """
        return self.__size * self.__size
