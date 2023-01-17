#!/usr/bin/python3
"""a class Square that inherits from Rectangle (9-rectangle.py):"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
     """A square class inherited from the Rectangle class"""
    def __init__(self, size):
        """Instantiation with size"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """returns the the format in string"""
        return super().__str__()

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

