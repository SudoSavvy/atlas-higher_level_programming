#!/usr/bin/python3
"""Module for Square class inheriting from Rectangle."""

from rectangle import Rectangle  # Assuming Rectangle is defined in rectangle.py

class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize the Square with size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)  # Initialize Rectangle with width and height both as size

    def area(self):
        """Return the area of the Square."""
        return self.__size * self.__size
