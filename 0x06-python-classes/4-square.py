#!/usr/bin/python3
"""A class called Square"""
class Square:
    """A class with a private object attribute"""
    def __init__(self, size = 0):
        """Method to initialize the square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        """Method that returns the area of the square
        """
        return self.__size ** 2
    @property
    def size(self):
        """ This method returns the size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        method to set the size value of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size ust be >= 0")
        else:
            self.__size = value
