#!/usr/bin/python3

def add(a, b):
    try:
        return a + b
    except TypeError:
        return None

result = add(98, "Holberton")
if result is not None:
    print(result)
