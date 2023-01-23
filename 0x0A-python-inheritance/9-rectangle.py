#!/usr/bin/python3
"""Geometry class"""
BaseGeometry = __import__('7-base_geometry'). BaseGeometry


class Rectangle(BaseGeometry):
    """A representation of a rectangle"""
    def __init__(self, width, height):
        """instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Method that computes area of Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Method that returns the description of the rectangle"""
        return "[{}] {}/{}".format(
                    self.__class__.__name__,
                    self.__width,
                    self.__height)
