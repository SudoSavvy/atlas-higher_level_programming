#!/usr/bin/python3

def add(a, b):
    try:
        return a + b
    except TypeError:
        return None

print(add(100, -2))
print(add(-100, -2))
print(add(0, 0))
print(add(98, "Holberton"))
print(add(1, 2))
