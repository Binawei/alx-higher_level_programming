#!/usr/bin/python3
"""This module Defines a class called Square"""
class Square:
     """
    A Square class with a private object attribute called size"""
    def __init__(self, size):
        """Instantiation wit a private attribute size
        args:
            size: the size of the square
        """
        self.__size = size
