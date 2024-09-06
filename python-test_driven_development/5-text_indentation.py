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
    Prints a text with two new lines after each of these characters: ., ? and :
    Arguments:
    text -- the text to be processed
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in ".?:":
            if i + 1 < len(text) and text[i + 1] == ' ':
                i += 1  # Skip the space after the punctuation
            result += '\n\n'
        i += 1
    
    # Remove any leading/trailing white spaces from each line
    print('\n'.join(line.strip() for line in result.split('\n')))

# For testing purposes:
if __name__ == "__main__":
    text = "Holberton School. How are you: John? This is a test."
    text_indentation(text)
