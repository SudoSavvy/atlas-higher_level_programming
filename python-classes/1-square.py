#!/usr/bin/python3
class Square:
    """
    A class that defines a square with a private size attribute.
    """

    def __init__(self, size):
        """
        Initialize the square with a given size.
        """
        self.__size = size #This is the private attribute.
        