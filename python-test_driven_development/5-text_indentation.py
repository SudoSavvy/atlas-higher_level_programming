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
            # Move to the next character and add new lines
            result += '\n\n'
            # Skip any spaces after the punctuation
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        i += 1

    # Remove leading and trailing spaces from each line
    lines = result.split('\n')
    cleaned_lines = [line.strip() for line in lines]
    final_result = '\n'.join(cleaned_lines)

    # Print the final result
    print(final_result, end="")

# For testing purposes:
if __name__ == "__main__":
    text = "Holberton School"
    text_indentation(text)
