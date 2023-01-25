#!/usr/bin/python3
"""This module a class Square that defines a square with
Private instance attribute: size
"""
class Square:
    """a class Square that defines a square"""
    def __init__(self, size=0):
        """Instantiates with a private attribute size.
        args:
            size: size of the sqaure which must be >0 and of type int.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
