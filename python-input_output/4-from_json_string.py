#!/usr/bin/python3
"""Module for converting a JSON string to a Python object."""

def from_json_string(my_str):
    """Convert a JSON string representation to a Python object.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The corresponding Python data structure.
    """
    def parse_value(value):
        """Parse a JSON value."""
        value = value.strip()
        if value.startswith('"') and value.endswith('"'):
            return value[1:-1]  # Remove surrounding quotes
        elif value == 'true':
            return True
        elif value == 'false':
            return False
        elif value == 'null':
            return None
        elif value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
            return int(value)
        try:
            return float(value)
        except ValueError:
            raise ValueError("Unsupported type")

    def parse_list(s):
        """Parse a JSON array."""
        items = s[1:-1].strip()
        if not items:
            return []
        result = []
        depth = 0
        start = 0
        for i, char in enumerate(items):
            if char == '[':
                depth += 1
            elif char == ']':
                depth -= 1
            elif char == ',' and depth == 0:
                result.append(parse_value(items[start:i].strip()))
                start = i + 1
        result.append(parse_value(items[start:].strip()))
        return result

    def parse_dict(s):
        """Parse a JSON object."""
        items = s[1:-1].strip()
        if not items:
            return {}
        result = {}
        key = ''
        value = ''
        in_key = True
        in_value = False
        depth = 0
        for char in items:
            if char == '{':
                depth += 1
            elif char == '}':
                depth -= 1
            elif char == ':' and depth == 0:
                in_key = False
                in_value = True
            elif char == ',' and depth == 0:
                result[key] = parse_value(value)
                key = ''
                value = ''
                in_key = True
                in_value = False
            else:
                if in_key:
                    key += char
                elif in_value:
                    value += char
        result[key] = parse_value(value)
        return result

    if my_str.startswith('[') and my_str.endswith(']'):
        return parse_list(my_str)
    elif my_str.startswith('{') and my_str.endswith('}'):
        return parse_dict(my_str)
    else:
        raise ValueError("Invalid JSON string format")

# Sample usage
if __name__ == "__main__":
    s_my_list = "[]"
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

    s_my_invalid = """
    {"is_active": true, 12 }
    """
    try:
        my_invalid = from_json_string(s_my_invalid)
        print(my_invalid)
        print(type(my_invalid))
    except ValueError as e:
        print(f"[{e.__class__.__name__}] {e}")
