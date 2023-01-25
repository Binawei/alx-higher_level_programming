#!/usr/bin/python3
"""
This module defines a Class Square and initialized with a private attributes size
"""
class Square:
    """a class Square that defines a square"""
    def __init__(self, size):
        """Instantiation with private attribute size
        args:
            the size of the square which is private
        """
        self.__size = size
