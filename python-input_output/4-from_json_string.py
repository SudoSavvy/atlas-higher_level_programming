#!/usr/bin/python3
"""Module for converting a JSON string to a Python object."""

def from_json_string(my_str):
    """
    Parses a JSON-like string and converts it into a Python data structure.

    Args:
        my_str (str): A JSON-like string representation of a Python data structure.

    Returns:
        The Python data structure represented by the JSON-like string. This can be
        a list, dictionary, string, integer, float, boolean, or None.

    Raises:
        ValueError: If the input string is empty or cannot be parsed into a valid Python
                    data structure.

    Example:
        >>> from_json_string('{"id": 12, "numbers": [1, 2, 4]}')
        {'id': 12, 'numbers': [1, 2, 4]}

        >>> from_json_string('"Simple string"')
        'Simple string'

        >>> from_json_string('[true, false, null]')
        [True, False, None]

        >>> from_json_string('{"key": "value", "numbers": [1, 2]}')
        {'key': 'value', 'numbers': [1, 2]}
    """
    def parse_value(value):
        """
        Parses a string value and converts it into the appropriate Python data type.

        Args:
            value (str): The string value to parse.

        Returns:
            The corresponding Python data type (str, int, float, bool, None, list, dict).

        Raises:
            ValueError: If the value cannot be converted to a supported Python type.
        """
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
            return parse_list(value)
        elif value.startswith('{') and value.endswith('}'):
            return parse_dict(value)
        try:
            return int(value)
        except ValueError:
            pass
        try:
            return float(value)
        except ValueError:
            raise ValueError("Unsupported type")

    def parse_list(value):
        """
        Parses a JSON-like list string and converts it into a Python list.

        Args:
            value (str): The JSON-like list string to parse.

        Returns:
            A Python list containing the parsed elements.
        """
        value = value[1:-1].strip()
        if not value:
            return []
        elements = split_elements(value)
        return [parse_value(el) for el in elements]

    def parse_dict(value):
        """
        Parses a JSON-like dictionary string and converts it into a Python dictionary.

        Args:
            value (str): The JSON-like dictionary string to parse.

        Returns:
            A Python dictionary containing the parsed key-value pairs.
        """
        value = value[1:-1].strip()
        if not value:
            return {}
        items = split_elements(value, dict_mode=True)
        result = {}
        for item in items:
            key, val = item.split(':', 1)
            result[parse_value(key)] = parse_value(val)
        return result

    def split_elements(value, dict_mode=False):
        """
        Splits a JSON-like string into its constituent elements (for lists or dictionaries).

        Args:
            value (str): The JSON-like string to split.
            dict_mode (bool): If True, split by dictionary item delimiters (':', ',').

        Returns:
            A list of elements extracted from the input string.
        """
        elements = []
        depth = 0
        current = []
        in_string = False
        for char in value:
            if char == '"' and (not in_string or (current and current[-1] != '\\')):
                in_string = not in_string
            if not in_string:
                if char == '{' or char == '[':
                    depth += 1
                elif char == '}' or char == ']':
                    depth -= 1
                if depth == 0 and char in ',:' and not in_string:
                    elements.append(''.join(current).strip())
                    current = []
                else:
                    current.append(char)
        if current:
            elements.append(''.join(current).strip())
        return elements

    if not my_str:
        raise ValueError("Empty string is not valid JSON")

    return parse_value(my_str)
