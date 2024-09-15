#!/usr/bin/python3
"""Module for loading an object from a JSON file."""

def load_from_json_file(filename):
    """Create an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        object: The Python data structure represented by the JSON content.
    """
    with open(filename, 'r') as file:
        content = file.read()
        # Manual JSON parsing using custom functions to avoid imports.
        return from_json_string(content)

def from_json_string(my_str):
    """Convert a JSON string representation to a Python object.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The corresponding Python data structure.
    """
    def parse_value(value):
        value = value.strip()
        if value == "true":
            return True
        elif value == "false":
            return False
        elif value == "null":
            return None
        elif value.startswith('"') and value.endswith('"'):
            return value[1:-1]
        elif value.startswith('[') and value.endswith(']'):
            return parse_array(value)
        elif value.startswith('{') and value.endswith('}'):
            return parse_dict(value)
        else:
            try:
                return int(value)
            except ValueError:
                try:
                    return float(value)
                except ValueError:
                    raise ValueError("Unsupported type")

    def parse_array(array_str):
        array_str = array_str[1:-1].strip()
        elements = split_elements(array_str)
        return [parse_value(element) for element in elements]

    def parse_dict(dict_str):
        dict_str = dict_str[1:-1].strip()
        items = split_items(dict_str)
        result = {}
        for item in items:
            key, value = item.split(':', 1)
            key = parse_value(key.strip())
            value = parse_value(value.strip())
            result[key] = value
        return result

    def split_elements(s):
        depth = 0
        result = []
        current = []
        for char in s:
            if char in '[]{}':
                if char in '[{':
                    depth += 1
                elif char in ']}':
                    depth -= 1
            if char == ',' and depth == 0:
                result.append(''.join(current).strip())
                current = []
            else:
                current.append(char)
        if current:
            result.append(''.join(current).strip())
        return result

    def split_items(s):
        depth = 0
        result = []
        current = []
        in_quotes = False
        for char in s:
            if char == '"':
                in_quotes = not in_quotes
            if char in '[]{}':
                if char in '[{':
                    depth += 1
                elif char in ']}':
                    depth -= 1
            if char == ',' and depth == 0 and not in_quotes:
                result.append(''.join(current).strip())
                current = []
            else:
                current.append(char)
        if current:
            result.append(''.join(current).strip())
        return result

    my_str = my_str.strip()
    if my_str.startswith('[') and my_str.endswith(']'):
        return parse_array(my_str)
    elif my_str.startswith('{') and my_str.endswith('}'):
        return parse_dict(my_str)
    elif my_str.startswith('"') and my_str.endswith('"'):
        return my_str[1:-1]
    else:
        raise ValueError("Unsupported JSON string format")
