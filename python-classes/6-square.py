#!/usr/bin/python3
"""
This module defines a Square class with private size and position attributes.
The class includes validation to ensure size is an integer >= 0 and position is a
tuple of two positive integers.
It provides methods to calculate the area of the square and print the square using
the character #.
"""


class Square:
    """
    A class that defines a square with private size and position attributes.
    Provides methods to get and set these attributes with validation,
    calculate the area of the square, and print the square with # at a specific
    position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the square with a given size and position.
        Size must be an integer and >= 0.
        Position must be a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieve the current position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.
        Position must be a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square with the character # at a specific position.
        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print()
            return

        # Print leading rows based on vertical position
        for _ in range(self.__position[1]):
            print()

        # Print the square
        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)
