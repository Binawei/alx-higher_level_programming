#!/usr/bin/python3
"""
This module is about a class Rectangle that inherits from the Base
class
"""
from base import Base

class Rectangle(Base):
    """A Rectangle class that inherits from the Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    
    @property
    def width(self):
        """
        Returns the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """This methods sets the method to value"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value


    @property
    def height(self):
        """Returns the height of the Rectangle"""
        return self.__height


    @height.setter
    def height(self, value):
        """Sets the height to value"""
        if type(value) != int:
            raise TypeError("height must be an integer")       
        if value <= 0:                                                    
            raise ValueError("height must be > 0")                   
        self.__height = value

    @property
    def x(self):
        """returns the value of the x cordinates of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x to value"""
        if type(value) != int:      
            raise TypeError("x must be an integer")        
        if value < 0:                                           
            raise ValueError("x must be >= 0")                 
        self.__x = value

    @property
    def y(self):
        """Returns the y cordinates of the rectangle"""
        return self.__y
   
    @y.setter
    def y(self, value):
        """sets y to value"""
        if type(value) != int:           
            raise TypeError("y must be an integer")         
        if value < 0:                      
            raise ValueError("y must be >= 0")            
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self._height


    def display(self):
        """that prints in stdout the Rectangle instance with the
        character #"""
        rectangle = self.__y * "\n"
        for i in range(self.__height):
            rectangle += (" " * self.__x)
            rectangle += ("#" * self.__width) + "\n"
        print(rectangle, end='')

    def update(self, *args, **kwargs):
        """Assignes an argument to each attribute"""
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'width','height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
               setattr(self, key, value)
       
  
    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y,
                                   self.__width, self.__height)


    def to_dictionary(self):
        """Returns the dictionary representation of the class Rectangle"""
        my_attr = ['id', 'width', 'height', 'x', 'y']
        my_dict = {}
        for key in my_attr:
            my_dict[key] = getattr(self, key)
        return my_dict



if __name__ == "__main__":
    r1 = Rectangle(10, 2, 1, 9)
    print(r1)
    r1_dictionary = r1.to_dictionary()
    print(r1_dictionary)
    print(type(r1_dictionary))

    r2 = Rectangle(1, 1)
    print(r2)
    r2.update(**r1_dictionary)
    print(r2)
    print(r1==r2)
