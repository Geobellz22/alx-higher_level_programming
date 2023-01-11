#!/usr/bin/python3
"""Verify object class inheritance"""


def is_kind_of_class(obj, a_class):
    """Checks if the object is an instance of, or if the object is an instance
    of a class that inherited from the specified class
    Args:
        obj (a_class): object to be checked
        a_class (class): The class of the object given
      return: True if object is an instance of the a_class; False otherwise
    """
    return isinstance(obj, a_class)
