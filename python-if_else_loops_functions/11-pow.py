#!/usr/bin/python3
def pow(a, b):
    if b < 0:
        a = 1 / a
        b = -b
    result = 1.0
    for _ in range(b):
        result *= a
    if result == int(result):
        return int(result)
    return result
