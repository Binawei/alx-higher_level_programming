#!/usr/bin/python3
"""
This module writes a class Square that inherits from the Rectangle class
"""
from base import Base
from rectangle import Rectangle
class Square(Rectangle):
    """A class Square that inherits from the Rectangle class"""
    def __init__(self, size, x=0,y=0, id=None):
       super().__init__(size, size, x, y, id)
       self.__size = size
       self.__x = x
       self.__y = y

    def __str__(self):
        return "[Square] ({}) {}/{} -{}".format(self.id, self.__x, self.__y, self.__size)

    def area(self):
        """Overwrights the area method from the rectangle"""
        return self.__size ** 2

    def update(self, *args, **kwargs):
       """Assigns attributes to their respective arguments correspondingly"""
       if args is not None and len(args) is not 0:
           list_atr = ['id','size', 'x', 'y']
           for i in range(len(args)):
               setattr(self, list_atr[i], args[i])
       else:
           for key, value in kwargs.items():
               setattr(self, key, value)


    @property
    def size(self):
        """Returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of the square to value
        thereby overwriting the setter for the rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value


    def to_dictionary(self):
        """Returns the dictionary representation of the class Square
        and overwrites the methods in the Rectangle class"""
        my_attr = ['id', 'size', 'x', 'y']
        my_dict = {}

        for elem in my_attr:
            my_dict[elem] = getattr(self, elem)
        return my_dict


if __name__ == "__main__":
    s1 = Square(10, 2, 1)
    print(s1)

    s1_dictionary = s1.to_dictionary()
    print(s1_dictionary)
    print(type(s1_dictionary))

    s2 = Square(1, 1)
    print(s2)
    s2.update(**s1_dictionary)
    print(s2)
    print(s1==s2)

    s1.update(1, 2)
    print(s1)

    s1.update(1, 2, 3)
    print(s1)

    s1.update(1, 2, 3, 4)
    print(s1)

    s1.update(x=12)
    print(s1)

    s1.update(size=7, y=1)
    print(s1)

    s1.update(size=7, id=89, y=1)
    print(s1)   
