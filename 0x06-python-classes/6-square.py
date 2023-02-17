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
        else:
            self.__size = value
    @property
    def position(self):
         return self.__position
    @position.setter
    def position(self, value):
         if not isinstance(value, tuple) or len(value) != 2 or \ 
                not all(i >= 0 for i in value):
               raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = value
        
    def my_print(self):
        if self.__size == 0:
            print ()
            return
        for i in range(0, self.__position[1]):
            print("")
        for idx in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end='')
            for l in range(0, self.__size):
                print("#", end='')
            print("")
