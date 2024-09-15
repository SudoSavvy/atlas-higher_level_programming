#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list class.
It provides an additional method to print the list in ascending sorted order.
"""

class MyList(list):
    """A subclass of list that can print itself sorted in ascending order."""
    
    def print_sorted(self):
        """Prints the list elements in sorted (ascending) order."""
        print(sorted(self))
    
    def __str__(self):
        """Return a string representation of the list."""
        return super().__str__()
