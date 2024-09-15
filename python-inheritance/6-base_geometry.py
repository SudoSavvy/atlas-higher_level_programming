#!/usr/bin/python3
"""
6-base_geometry.py

This module defines the BaseGeometry class.
"""

class BaseGeometry:
    """
    A base class for geometric shapes.

    Methods:
        area(self): Raises an Exception indicating that the method is not implemented.
    """
    def area(self):
        """
        Method that raises an Exception with the message "area() is not implemented".

        Raises:
            Exception: with the message "area() is not implemented"
        """
        raise Exception("area() is not implemented")
