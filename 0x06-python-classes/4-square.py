#!/usr/bin/python3
"""Describes a square class"""


class Square:
    """Defines a square class"""
    def __init__(self, size=0):
        """initialize square
        Args:
            size (int): size of the square
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """defines the area of a square"""
        return (self.__size ** 2)
