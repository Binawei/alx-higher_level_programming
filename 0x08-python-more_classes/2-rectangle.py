#!/usr/bin/python3
"""a class Rectangle that defines a rectangle by:
(based on 0-rectangle.py)"""                                                    
class Rectangle:                                                                
    """a class Rectangle that defines a rectangle by"""         
    def __init__(self, width = 0, height = 0):                                  
        self.width = width                                                 
        self.height = height                                 

    @property                                                                                      
    def width(self):                                              
        """A method to retrieve the width using the knowledge 
        of getter"""                           
        return self.__width                                                 

    @width.setter    

    def width(self, value):                                                                                                             
        """A method to sets the value of the width to value"""                                                                          
        if type(value) != int:                                             
            raise TypeError("width must be an integer")         
        if value < 0:                                            
            raise ValueError("width must be >= 0")                             
        self.__width = value 

    def area(self):
        """A method to return the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 
        return 2 * (self.width + self.height)
