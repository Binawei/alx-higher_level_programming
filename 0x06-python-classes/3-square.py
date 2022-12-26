#!/usr/bin/python3
"""
    defines a class called Square
"""
class Square:
    """
        A Square class with a private object attribute.
        check the type of argument and raises error
    """
    def __init__(self, size = 0):
        if type(size) is not int:
             raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """
        A method that returns the area of the square
    """
    def area(self):
        return self.__size ** 2
