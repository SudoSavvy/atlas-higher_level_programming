#!/usr/bin/python3
def pow(a, b):
    if b < 0:
        a = 1 / a
        b = -b
    result = 1.0
    for _ in range(b):
        result *= a
    # Format the result to 2 decimal places if it is effectively an integer
    if result == int(result):
        return float(f"{result:.2f}")
    return float(f"{result:.10g}")
