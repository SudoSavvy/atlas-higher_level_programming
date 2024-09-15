#!/usr/bin/python3
"""Module for Rectangle class inheriting from BaseGeometry."""

from base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""
    
    def __init__(self, width, height):
        """Initialize the Rectangle with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"

    @property
    def width(self):
        """Return the width of the Rectangle."""
        return self.__width

    @property
    def height(self):
        """Return the height of the Rectangle."""
        return self.__height
