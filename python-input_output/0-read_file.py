#!/usr/bin/python3
"""Module for reading a text file and printing its contents."""

def read_file(filename=""):
    """Read a text file (UTF-8) and print its contents to stdout."""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')

