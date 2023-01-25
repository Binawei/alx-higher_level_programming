#!/usr/bin/python3
"""This module defines a class Square"""
class Square:
    """
    A class square that defines a square by its size
    """
    def __str__(self):
        """ String representation of the Square class"""
        ret = ""
        if self.__size == 0:
            return ret

        for i in range(self.position[1]):
            ret +="\n"

        for i in range(0, self.size):
            for k in range(self.position[0]):
                ret += " "
            for j in range(self.size):
                ret += "#"
            if i is not (sel.size - 1):
                ret += "\n"
        return ret

    def __init__(self, size=0, position=(0,0)):
        """Method to initialize the square object"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Returns the size value of the square object"""
        return self.__size

    @size.setter
    def size(self, value):
        """Method to set th size value of the square object"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
         elif value < 0:
            raise ValueError("size must be >= 0")
       self.__size = value

    @property
    def position(self):
        """Method to sets the position value of a square object"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 postive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value


    def area(self):
        """Method that returns the square area of the square object"""
        return self.__size ** 2

    def my_print(self):
        """Method that prints # square according to the size value"""
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                for k in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end='')
                print()
