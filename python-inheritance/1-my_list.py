#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list class.
It includes a method to print the list in ascending sorted order.
"""

class MyList(list):
    """
    A subclass of the built-in list class that provides a method to print
    the list sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.

        Assumes all elements in the list are integers.
        """
        print(sorted(self))
