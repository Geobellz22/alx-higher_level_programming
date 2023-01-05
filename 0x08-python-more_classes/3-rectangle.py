#!/usr/bin/python3
"""A Rectangle class"""


class Rectangle:
    """Defines a Rectangle class"""

    def __init__(self, width=0, height=0):
        """Instantiates a Rectangle object
        Args:
            width (int) width of the rectangle
            height (int) height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.width == 0:
            return 0
        elif self.height == 0:
            return 0
        else:
            return self.__height + self.__height + self.__width + self.__width

    def __str__(self):
        if self.__height or self.__width == 0:
            return ("")
        return (("#" * self.__width) +
 ("\n" + "#" * self.__width) * (self.__height - 1))
