#!/usr/bin/python3
def pow(a, b):
    if b < 0:
        a = 1 / a
        b = -b
    result = 1.0
    for _ in range(b):
        result *= a
    # Ensure the result is formatted to the maximum precision required
    return "{:.15e}".format(result)
