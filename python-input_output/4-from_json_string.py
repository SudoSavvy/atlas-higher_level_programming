#!/usr/bin/python3
"""Module for converting a JSON string to a Python object."""

def from_json_string(my_str):
    """Convert a JSON string representation to a Python object.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The corresponding Python data structure.
    """
    if my_str.startswith('[') and my_str.endswith(']'):
        # Handle list
        items = my_str[1:-1].split(', ')
        result = []
        for item in items:
            if item.startswith('"') and item.endswith('"'):
                result.append(item[1:-1])
            else:
                try:
                    result.append(int(item))
                except ValueError:
                    try:
                        result.append(float(item))
                    except ValueError:
                        result.append(item)
        return result
    
    elif my_str.startswith('{') and my_str.endswith('}'):
        # Handle dictionary
        items = my_str[1:-1].split(', ')
        result = {}
        for item in items:
            key, value = item.split(': ')
            if key.startswith('"') and key.endswith('"'):
                key = key[1:-1]
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            elif value == 'true':
                value = True
            elif value == 'false':
                value = False
            elif value == 'null':
                value = None
            else:
                try:
                    value = int(value)
                except ValueError:
                    try:
                        value = float(value)
                    except ValueError:
                        pass  # Keep as string if it fails to convert
            result[key] = value
        return result

    else:
        raise ValueError("Invalid JSON string format")

# Sample usage
if __name__ == "__main__":
    s_my_list = "[1, 2, 3]"
    my_list = from_json_string(s_my_list)
    print(my_list)
    print(type(my_list))

    s_my_dict = """
    {"is_active": true, "info": {"age": 36, "average": 3.14}, 
    "id": 12, "name": "John", "places": ["San Francisco", "Tokyo"]}
    """
    my_dict = from_json_string(s_my_dict)
    print(my_dict)
    print(type(my_dict))
