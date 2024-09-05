#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute.
The class includes validation to ensure size is an integer and >= 0,
getter and setter methods to access and update the size,
and methods to compute the area and print the square.
"""


class Square:
    """
    A class that defines a square with a private size attribute.
    Provides methods to get and set the size with validation,
    calculate the area of the square, and print the square with #.
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

    def my_print(self):
        """
        Print the square with the character #.
        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)
