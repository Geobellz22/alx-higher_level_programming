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

    def to_json(self):
        """retrieves a dictionary representation of a student instance"""
        return self.__dict__
