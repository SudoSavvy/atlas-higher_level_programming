#!/usr/bin/python3
"""Module for writing a string to a text file and returning the number of characters written."""

def write_file(filename="", text=""):
    """Write a string to a text file (UTF-8) and return the number of characters written."""
    with open(filename, 'w', encoding='utf-8') as file:
        nb_characters_written = file.write(text)
    return nb_characters_written
