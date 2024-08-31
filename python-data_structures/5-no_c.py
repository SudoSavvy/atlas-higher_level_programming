#!/usr/bin/python3
def no_c(my_string):
    # Create a new string without 'c' or 'C' by iterating through the original string
    new_string = ''.join([char for char in my_string if char not in 'cC'])
    return new_string
