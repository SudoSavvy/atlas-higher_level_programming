#!/usr/bin/python3
"""Module for Rectangle class inheriting from BaseGeometry."""

class BaseGeometry:
    """BaseGeometry class with basic validation methods."""

    def integer_validator(self, name, value):
        """Validate if value is an integer greater than zero."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize the Rectangle with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        """Return a formal string representation of the Rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
