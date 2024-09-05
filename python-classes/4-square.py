#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute.
The class includes validation to ensure size is an integer and >= 0,
with getter and setter methods to access and update the size.
It also provides a method to compute the area of the square.
"""


class Square:
    """
    A class that defines a square with a private size attribute.
    Provides methods to get and set the size with validation,
    and to calculate the area of the square.
    """

    def __init__(self, size=0):
        """
        Initialize the square with a given size.
        Size must be an integer and >= 0.
        """
        self.size = size  # Use the setter to apply validation

    @property
    def size(self):
        """
        Retrieve the current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.
        Value must be an integer and >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.
        """
        return self.__size * self.__size
