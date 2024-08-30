#!/usr/bin/python3
def islower(c):
    ascii_value = ord(c)
    
    if ord('a') <= ascii_value <= ord('z'):
        return True
    else:
        return False
