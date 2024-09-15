#!/usr/bin/python3
"""
This module defines the MyList class, which inherits from list.
"""

class MyList(list):
    """
    A subclass of list with an additional method to print the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order without modifying the original list.
        """
        print(sorted(self))
