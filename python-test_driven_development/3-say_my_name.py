#!/usr/bin/python3
"""
This module defines the function `say_my_name`.

The function prints a formatted string:
'My name is <first name> <last name>'

Raises:
    TypeError: If `first_name` or `last_name` is not a string.
"""

def say_my_name(first_name, last_name=""):
    """Prints 'My name is <first name> <last name>'.

    Args:
        first_name (str): The first name.
        last_name (str): The last name, default is an empty string.

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    # Print the formatted name
    print(f"My name is {first_name} {last_name}")
