#!/usr/bin/python3
"""Module for appending a string to a text file and returning the number of characters added."""

def append_write(filename="", text=""):
    """Append a string to a text file (UTF-8) and return the number of characters added."""
    with open(filename, 'a', encoding='utf-8') as file:
        nb_characters_added = file.write(text)
    return nb_characters_added
