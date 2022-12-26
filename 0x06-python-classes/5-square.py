#!/usr/bin/python3
"""Defines a class called Square"""
class Square:
    """
    initializes the class with a private object called size
    """
    def __init__(self, size):
        """checks the type of the size and initializes it"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Method that returns the area of the square
        """
        return self.__size ** 2
    @property
    def size(self):
        """Method to return the size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """Method to set the size value of the square objects
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value


    def my_print(self):
        """Method that print  a # suare according to the size"""
        if not self.__size:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()

