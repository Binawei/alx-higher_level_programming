#!/usr/bin/python3                                                                                                                      
"""                                                                                                                                     
A rectangle with width and height.                                                                                                     
"""                                                                                                                                     
class Rectangle:                                                                                                                       
    """                                                                                                                                 
    Rectangle functions and data                                                                                                        
    """                                                                                                                                 
    number_of_instances = 0                                                                                                            
    print_symbol = '#'                                                                                                                  

    def __init__(self, width=0, height=0):                                                                                              
        """ Instantiation                                                                                                               
        """                                                                                                                            
        type(self).number_of_instances += 1                                                                                             
        self.width = width                                                                                                             
        self.height = height                                                                                                            

    @property                                                                                                                           
    def width(self):                                                                                                                   
        """Returns the width"""                                                                                                         
        return self.__width                                                                                                             

                                                                                                                                        
    @width.setter                                                                                                                       
    def width(self, value):                                                                                                             
        """ Setter for width to value"""                                                                                                
        if type(value) != int:                                                                                                          
            raise TypeError("width must be an integer")                                                                                 
        if value < 0:                                                                                                                   
            raise ValueError("width must be >= 0")                                                                                      
        self.__width = value                                                                                                            
                                                                                                                                        

    @property                                                                                                                           
    def height(self):                                                                                                                   

        """ Getter for height                                                                                                          
        """                                                                                                                             
        return self.__height                                                                                                      

    @height.setter
    def height(self, value):                                                                                                            
        """ Setter for height                                                                                                          
        """                                                                                                                             
        if type(value) != int:                                                                                                          
            raise TypeError("width must be an integer")                                                                                 
        if value < 0:                                                                                                                  
            raise ValueError("height must be >= 0")                                                                                     
        self.__height = value                                                                                                           

    def area(self):                                                                                                                    
        """ Returns area of rectangle                                                                                                   
        """                                                                                                                             
        return self.__width * self.__height                                                                                             
                                                                                                                                        

    def perimeter(self):                                                                                                               
        """ Returns perimeter of rectangle                                                                                              
        """                                                                                                                             
        if self.__width == 0 or self.__height == 0:                                                                                     
            return 0                                                                                                                    
        else:                                                                                                                          
            return 2 * (self.__width + self.__height)                                                                                   

    def __str__(self):                                                                                                                  
        """ print() __str__ method funtion to return rectangle i                                                                        
        """                                                                                                                             
        res = ""                                                                                                                        
        if self.__width == 0 or self.__height == 0:                                                                                     
            return res                                                                                                                  

        for i in range(self.__height):                                                                                                  
            for j in range(self.__width):                                                                                               
                res += str(self.print_symbol)                                                                                           
            if i != self.__height - 1:                                                                                                  
                res += '\n'                                                                                                             
        return res                                                                                                                      

                                                                                                                                        
    def __repr__(self):                                                                                                                 
        """ print() or eval() __repr__ method functioon return                                                                          
            ... Rectangle(width, height)                                                                                                
        """                                                                                                                             
        w = str(self.__width)                                                                                                           
        h = str(self.__height)                                                                                                          
        res = "Rectangle(" + w + ", " + h + ")"                                                                                         
        return res                                                                                                                      
                                                                                                                                        

    @staticmethod                                                                                                                       
    def bigger_or_equal(rect_1, rect_2):                                                                                                
        """This methods compare the objects ot two rectangles                                                                           
        and returns the biggest rectangle based on the area"""                                                                          
        if not isinstance(rect_1, Rectangle):                                                                                           
            raise TypeError("rect_1 must be an instance of Rectangle")                                                                  
        if not isinstance(rect_2, Rectangle):                                                                                           
            raise TypeError("rect_2 must be an instance of Rectangle")                                                                  
        if rect_1.area() > rect_2.area():                                                                                               
            return rect_1                                                                                                               
        elif rect_1.area() == rect_2.area():                                                                                            
            return rect_1                                                                                                               
        else:                                                                                                                           
            return rect_2                                                                                                              

    @classmethod
    def square(cls, size=0):
        """
        Method returns a new Rectangle instance with width == height == size
        """
        width = height = size
        return cls(width, height)
                                                                                                                                        

    def __del__(self):                                                                                                                  
        print("Bye rectangle"+"...")                                                                                                    
        type(self).number_of_instances -= 1                                                  
