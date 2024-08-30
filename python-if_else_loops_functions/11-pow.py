#!/usr/bin/python3
def pow(a, b):
    if b < 0:
        a = 1 / a
        b = -b
    result = 1.0
    for _ in range(b):
        result *= a
    # Adjust the output to be consistent with floating-point representation
    return float(f"{result:.10g}")
