#!/usr/bin/python3
"""Defines a class"""
class Square:
    """A class called Square instantiates by private objects"""
    def __init__(self, size = 0, position = (0, 0)):
        """Method that instantiatesnthe the class with private objects
        the objects are size and position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Method that retrieves the size value of the square"""
        return self.__size
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
             raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Method that returns the position value of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Method that sets the value of position in the square
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Method that returns the current squared area"""
        return self.__size ** 2

    def my_print(self):
        """
        Method that prints in stdout the square with the character #
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__position[1]):
                print()
            for k in range(0, self.__size):
                for space in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print()
