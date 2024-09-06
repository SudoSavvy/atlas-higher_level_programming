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
        if text[i] in ('.', '?', ':'):
            formatted_text += text[i]
            formatted_text += '\n\n'
            # Skip additional spaces after punctuation
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        else:
            formatted_text += text[i]
        i += 1
    
    # Remove leading and trailing spaces from each line and print
    lines = formatted_text.strip().split('\n')
    for line in lines:
        print(line.strip())
