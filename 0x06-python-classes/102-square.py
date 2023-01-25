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

                                                                                                                                        
    def area(self):                                                                                                                     
        """
        Returns the current square area.                                                                                                
        args:                                                                                                                           
            self: the calling instance                                                                                                  
        """                                                                                                                             
        return self.__size ** 2

    def __eq__(self, other):
        """method to compare the equality of two objects"""
        return self.__size == other.__size

    def __ne__(self, other):
        """compares the nonequality of two objects"""
        return self.__size != other.__size

    def __gt__(self, other):
        return self.__size > other.__size

    def __ge__(self, other):
        return self.__size >= other.__size

    def __lt__(self, other):
        return self.__size < other.__size

    def __le__(self, other):
        return self.__size <= other.__size                                                                                                 
                                                                                                                                        
    @property                                                                                                                           
    def size(self):                                                                                                                     
        """Retrieves the size of the square so returns it"""                                                                            
        return self.__size                                                                                                              

                                                                                                                                        

    @size.setter                                                                                                                        
    def size(self, value):                                                                                                              
        """Sets the value of the size to value"""                                                                                       
        if type(value) != int:                                                                                                          
            raise TypeError("size must be an integer")                                                                                  
        elif value < 0:                                                                                                                 
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
