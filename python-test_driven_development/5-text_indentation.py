#!/usr/bin/python3
"""
Module: 5-text_indentation

This module contains a function `text_indentation` that formats text by adding two new lines after each of these characters: '.', '?', and ':'. It also trims leading and trailing spaces from each printed line.

Function:
- text_indentation(text): Prints the formatted text.

Raises:
- TypeError: If `text` is not a string.
"""

def text_indentation(text):
    """
    Prints text with two new lines after each '.', '?', and ':'.
    
    Args:
        text (str): The text to format and print.
        
    Raises:
        TypeError: If `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    for char in text:
        result += char
        if char in ('.', '?', ':'):
            result += "\n\n"

    for line in result.strip().split("\n"):
        print(line.strip())
