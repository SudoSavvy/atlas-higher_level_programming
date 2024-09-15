#!/usr/bin/python3
"""class MyList that inherits from list and prints sorted list"""


class MyList(list):
    """init class MyList with inheritance"""
    def print_sorted(self):
        """define function print_sorted(self)"""
        print(sorted(self))