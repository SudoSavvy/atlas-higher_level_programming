#!/usr/bin/python3
"""Module for converting an object to a JSON string."""

def to_json_string(my_obj):
    """Convert an object to a JSON string representation.

    Args:
        my_obj (object): The object to convert to JSON string.

    Returns:
        str: The JSON string representation of the object.
    """
    if isinstance(my_obj, str):
        return '"' + my_obj.replace('"', '\\"') + '"'
    elif isinstance(my_obj, int):
        return str(my_obj)
    elif isinstance(my_obj, float):
        return str(my_obj)
    elif isinstance(my_obj, bool):
        return 'true' if my_obj else 'false'
    elif isinstance(my_obj, list):
        return '[' + ', '.join(to_json_string(item) for item in my_obj) + ']'
    elif isinstance(my_obj, dict):
        items = []
        for key, value in my_obj.items():
            if not isinstance(key, str):
                raise TypeError("Keys must be strings")
            key_str = to_json_string(key)
            value_str = to_json_string(value)
            items.append(f'{key_str}: {value_str}')
        return '{' + ', '.join(items) + '}'
    elif isinstance(my_obj, set):
        raise TypeError("Object of type set is not JSON serializable")
    else:
        raise TypeError("Unsupported type")

# Sample usage or test
if __name__ == "__main__":
    data = { 'id': 3, 'title': "Holberton", 89 }  # This should raise an error for unsupported type
    print(to_json_string(data))
