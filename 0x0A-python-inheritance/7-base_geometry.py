#!/usr/bin/python3                                                                                                                      
"""Module 6-base_geometry.                                                                                                              
creates a class                                                                                                                         
"""
class BaseGeometry:                                                                                                                     
    """                                                                                                                                 
    class with public instance method.                                                                                                  
    """                                                                                                                                 
    def area(self):                                                                                                                     
        """                                                                                                                             
        raises an Exception with the message area() is not implemented                                                                  
        """                                                                                                                             
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        that validates value
        if value is not an integer: raise a TypeError exception, with
        the message <name> must be an integer
        if value is less or equal to 0: raise a ValueError exception with
        the message <name> must be greater than 0
        """
        self.name = name
        self.value = value
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
