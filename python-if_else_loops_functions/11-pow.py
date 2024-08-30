#!/usr/bin/python3
def pow(a, b):
    if b < 0:
        a = 1 / a
        b = -b
    result = 1.0
    for _ in range(b):
        result *= a
    # Format the result to handle precision correctly
    if result == int(result):
        return "{:.0f}".format(result)
    return "{:.10f}".format(result).rstrip('0').rstrip('.')
