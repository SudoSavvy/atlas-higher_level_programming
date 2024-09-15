#!/usr/bin/python3
"""
Making a sub sub class
"""

rec = __import__("9-rectangle").Rectangle


class Square(rec):
    """
    This is a sub class of rectangle
    It shows a square
    """

    def __init__(self, size):
        self.__size = self.integer_validator("size", size)

    def area(self):
        return self.__size**2