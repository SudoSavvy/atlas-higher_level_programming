#!/usr/bin/python3
"""Module for converting a JSON string to a Python object."""

class JSONDecodeError(ValueError):
    """Custom exception for JSON decode errors."""
    pass

def from_json_string(my_str):
    """Convert a JSON string representation to a Python object.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The corresponding Python data structure.

    Raises:
        JSONDecodeError: If the input string is not a valid JSON-like format.
    """
    def parse_value(value):
        """Parse and convert a string value to the appropriate Python data type.

        Args:
            value (str): The string to parse.

        Returns:
            The corresponding Python data type (str, int, float, bool, None, list, dict).

        Raises:
            JSONDecodeError: If the value cannot be converted to a supported Python type.
        """
        value = value.strip()
        if value == "true":
            return True
        elif value == "false":
            return False
        elif value == "null":
            return None
        elif value.startswith('"') and value.endswith('"'):
            return value[1:-1]  # Remove surrounding quotes for strings
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
                    raise JSONDecodeError("Unsupported type")

    def parse_array(array_str):
        """Parse a JSON-like array string and convert it into a Python list.

        Args:
            array_str (str): The JSON-like array string to parse.

        Returns:
            list: The corresponding Python list.
        """
        array_str = array_str[1:-1].strip()  # Remove surrounding brackets
        if not array_str:
            return []
        elements = split_elements(array_str)
        return [parse_value(element) for element in elements]

    def parse_dict(dict_str):
        """Parse a JSON-like dictionary string and convert it into a Python dictionary.

        Args:
            dict_str (str): The JSON-like dictionary string to parse.

        Returns:
            dict: The corresponding Python dictionary.
        
        Raises:
            JSONDecodeError: If the dictionary string is malformed.
        """
        dict_str = dict_str[1:-1].strip()  # Remove surrounding braces
        if not dict_str:
            return {}
        items = split_items(dict_str)
        result = {}
        for item in items:
            if ':' not in item:
                raise JSONDecodeError(f"Expecting ':' delimiter: {item}")
            key, value = item.split(':', 1)
            key = parse_value(key.strip())
            value = parse_value(value.strip())
            result[key] = value
        return result

    def split_elements(s):
        """Split a JSON-like string into individual elements (for arrays).

        Args:
            s (str): The JSON-like string to split.

        Returns:
            list: The list of elements.
        """
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
        """Split a JSON-like string into individual items (for dictionaries).

        Args:
            s (str): The JSON-like string to split.

        Returns:
            list: The list of items.
        """
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

    # Remove surrounding whitespaces
    my_str = my_str.strip()
    
    # Start parsing based on the type of JSON object
    if my_str.startswith('[') and my_str.endswith(']'):
        return parse_array(my_str)
    elif my_str.startswith('{') and my_str.endswith('}'):
        return parse_dict(my_str)
    elif my_str.startswith('"') and my_str.endswith('"'):
        return my_str[1:-1]  # Remove surrounding quotes for strings
    else:
        raise JSONDecodeError("Unsupported JSON string format")

# Sample usage
if __name__ == "__main__":
    s_data = '"Simple string"'
    data = from_json_string(s_data)
    print(data)
    print(type(data))
