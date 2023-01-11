#!/usr/bin/python3
"""Check object instance"""


def is_same_class(obj, a_class):
    """Checks if the object is exactly an instance of the specified class
    Args:
        obj (a_class): object to be checked
        a_class (class): The class of the object given

        return: True if object is an instance of the specified class; otherwise
    """
    return True if type(obj) is a_class else False
