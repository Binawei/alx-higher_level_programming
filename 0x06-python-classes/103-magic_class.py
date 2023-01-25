#!/usr/bin/python3
"""This module Defines a MagicClass that does exactly as the bytecode provided"""

from math import pi

class MagicClass:
    """Class that stores the properties of the circumfeence"""
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be q number")
        self.__radius = radius


    def area(self):
        """Method that calculates the area of the circumfernce"""
        return (self.__raduis ** 2) * pi

    def circumference(self):
        """Method that calculates the perimeter of the circumference"""
        return (2 * pi * self.__radius)
