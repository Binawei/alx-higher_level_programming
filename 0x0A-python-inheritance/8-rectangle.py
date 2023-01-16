#!/usr/bin/python3
"""Module 8-rectangle. create a rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represents a rectangle. private instance attributes:
        -width
        -height
    inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """Initializes an instance.
        Args:
        -width: width of the rectangle
        -height: height of the rectangle
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)                                                                                                  
        self.integer_validator("height", height) 

