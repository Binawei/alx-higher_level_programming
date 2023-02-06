#!/usr/bin/python3
"""this module writes a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represents a rectangle
    privares instance attributes are;
        -width: width of the rectangle
        -height: height of the rectangle
    public method area() inherited from BaseGeometty
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height


    def area(self):
        """Area that overides the Geometry area method"""
        return self.__height * self.__width


    def __str__(self):
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
