#!/usr/bin/python3
"""
Contains class "student"
"""


class Student:
    """Representation of student"""
    def __init__(self, first_name, last_name, age):
        """iniializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.
        If attrs is a list of strings, represents only those attributes
        included in the list.
        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if type(attrs) is list and all(type(ele) is str for ele in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the student in instance"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except FileNotFoundError:
                pass
