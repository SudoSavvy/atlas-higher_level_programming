#!/usr/bin/python3
"""Module for saving an object to a text file in JSON format."""

def to_json_string(my_obj):
    """Convert a Python object to a JSON string representation.

    Args:
        my_obj (object): The Python object to convert.

    Returns:
        str: The JSON string representation of the object.

    Raises:
        TypeError: If the object is not serializable to JSON.
    """
    if isinstance(my_obj, dict):
        items = [f'"{key}": {to_json_string(value)}' for key, value in my_obj.items()]
        return '{' + ', '.join(items) + '}'
    elif isinstance(my_obj, list):
        items = [to_json_string(item) for item in my_obj]
        return '[' + ', '.join(items) + ']'
    elif isinstance(my_obj, str):
        return f'"{my_obj}"'
    elif isinstance(my_obj, bool):
        return 'true' if my_obj else 'false'
    elif my_obj is None:
        return 'null'
    elif isinstance(my_obj, (int, float)):
        return str(my_obj)
    else:
        raise TypeError(f'Object of type {type(my_obj).__name__} is not JSON serializable')

def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation.

    Args:
        my_obj (object): The object to write to the file.
        filename (str): The name of the file to write to.

    The function converts the Python object to a JSON string and writes it to the specified file.
    """
    json_string = to_json_string(my_obj)
    with open(filename, 'w') as file:
        file.write(json_string)
