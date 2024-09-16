#!/usr/bin/python3
"""
This module defines a Student class with serialization and deserialization capabilities.
"""

class Student:
    """
    Defines a student with first name, last name, and age.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of attribute names (strings) to retrieve.
                                    If not provided or not a list, returns all attributes.

        Returns:
            dict: A dictionary representation of the Student instance, 
                  either with all attributes or selected ones.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance based on a dictionary.

        Args:
            json (dict): A dictionary with keys that match the attributes of the Student instance
                         and values that are the new values for those attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)
