#!/usr/bin/python3
""""This module is about a class Square that inherits from Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """"
    inherits from Rectangle (9-rectangle.py
    args:
        -size: the size of the rectangle
    """
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)


    def area(self):
        """Uses the area() method from rectangle"""
        return super().area()

    def __str__(self):
        return str("[Square] {}/{}".format(self.__size, self.__size))

