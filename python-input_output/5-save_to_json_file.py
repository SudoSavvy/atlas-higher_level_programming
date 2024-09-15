#!/usr/bin/python3

def to_json_string(my_obj):
    """Convert a Python object to a JSON string representation.

    Args:
        my_obj (object): The Python object to convert.

    Returns:
        str: The JSON string representation of the object.
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
    """
    json_string = to_json_string(my_obj)
    with open(filename, 'w') as file:
        file.write(json_string)

# Sample usage
if __name__ == "__main__":
    filename = "my_list.json"
    my_list = [1, 2, 3]
    save_to_json_file(my_list, filename)

    filename = "my_dict.json"
    my_dict = { 
        'id': 12,
        'name': "John",
        'places': ["San Francisco", "Tokyo"],
        'is_active': True,
        'info': {
            'age': 36,
            'average': 3.14
        }
    }
    save_to_json_file(my_dict, filename)

    try:
        filename = "my_set.json"
        my_set = {132, 3}
        save_to_json_file(my_set, filename)
    except Exception as e:
        print("[{}] 
