#!/usr/bin/python3
"""Describes a square class"""


class Square:
    """Defines a square class"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        def area(self):

            return (self.__size **2)
