#!/usr/bin/python3
"""
This script adds all arguments to a Python list, then saves them to a file.

It uses the functions `save_to_json_file` and `load_from_json_file` to handle JSON
file operations. The list is saved in a JSON representation in a file called `add_item.json`.
If the file doesn't exist, it will be created.
"""

def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file, using a JSON representation.

    Args:
        my_obj (object): The object to write to the file.
        filename (str): The name of the file to write to.
    """
    with open(filename, 'w') as file:
        json_str = to_json(my_obj)
        file.write(json_str)

def load_from_json_file(filename):
    """
    Load an object from a text file containing JSON representation.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        object: The Python object from the JSON file.
    """
    with open(filename, 'r') as file:
        json_str = file.read()
        return from_json(json_str)

def to_json(obj):
    """
    Convert a Python object to a JSON string.

    Args:
        obj (object): The Python object to convert to JSON.

    Returns:
        str: A JSON string representation of the object.
    """
    if isinstance(obj, dict):
        items = [f'"{key}": {to_json(value)}' for key, value in obj.items()]
        return '{' + ', '.join(items) + '}'
    elif isinstance(obj, list):
        elements = [to_json(element) for element in obj]
        return '[' + ', '.join(elements) + ']'
    elif isinstance(obj, str):
        return f'"{obj}"'
    elif isinstance(obj, bool):
        return 'true' if obj else 'false'
    elif isinstance(obj, (int, float)):
        return str(obj)
    elif obj is None:
        return 'null'
    else:
        raise TypeError("Object type not serializable")

def from_json(json_str):
    """
    Convert a JSON string to a Python object.

    Args:
        json_str (str): The JSON string to convert.

    Returns:
        object: A Python object.
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

    return parse_value(json_str.strip())

# Main logic to handle command-line arguments
if __name__ == "__main__":
    filename = "add_item.json"
    try:
        # Try to load the existing list from the file
        items = load_from_json_file(filename)
    except FileNotFoundError:
        # If file doesn't exist, start with an empty list
        items = []

    # Add all command-line arguments to the list
    from sys import argv
    items.extend(argv[1:])

    # Save the updated list to the file
    save_to_json_file(items, filename)
