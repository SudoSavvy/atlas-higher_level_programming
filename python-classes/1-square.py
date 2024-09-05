#!/usr/bin/python3
"""
This module defines a class Square.
The Square class represents a square with a private size attribute.
"""

class Square:
    """
    A class that defines a square with a private size attribute.
    """

    def __init__(self, size):
        """
        Initialize the square with a given size.
        """
        self.__size = size  # This is the private attribute.
