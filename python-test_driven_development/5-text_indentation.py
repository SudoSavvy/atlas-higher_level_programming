#!/usr/bin/python3
"""
Module: 5-text_indentation

This module contains a function `text_indentation` that formats text by adding two new lines after each '.', '?', and ':'. It also ensures that there is no leading or trailing space on each printed line.

Function:
- text_indentation(text): Formats and prints the text with the specified indentations.

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
    
    formatted_text = ""
    i = 0
    while i < len(text):
        formatted_text += text[i]
        if text[i] in ('.', '?', ':'):
            if i + 1 < len(text) and text[i + 1] == ' ':
                formatted_text += '\n\n'
                i += 1
            else:
                formatted_text += '\n\n'
        i += 1

    for line in formatted_text.strip().split("\n"):
        print(line.strip())
