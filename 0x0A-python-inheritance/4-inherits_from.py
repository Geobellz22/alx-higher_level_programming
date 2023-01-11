#!/usr/bin/python3
"""Checks for a subclass"""


def inherits_from(obj, a_class): 
 """Checks if the object is an instance of the class that inherited
    (directly or indirectly of a specified class)
    Args:
        obj (a_class):
        a_class (class):
    return:
    True if object is an instance of an inherited class, otherwise False
    """
 return not type(obj) is a_class and issubclass(type(obj), a_class)
