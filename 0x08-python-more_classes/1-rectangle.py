#!/usr/bin/python3
"""a class Rectangle that defines a rectangle by:
(based on 0-rectangle.py)"""
class Rectangle:
    """a class Rectangle that defines a rectangle by"""
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """A method to retrieve the width using the knowledge
        of getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """A method to sets the value of the width to value"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """A method to retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Amethod to set the value of the height to value"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
