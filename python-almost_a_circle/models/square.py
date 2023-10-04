""" A class Square that inherits from Rectangle 
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """ A class Square that inherits from class Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize Rectangle with private instance attributes
        width, height, x and y
        """
        self.__id = id
        super().__init__(size, size, x=0, y=0, id=None)
        

        
        """ Validate and instantiate size with condition:
            ~ must be an integer
            ~ must be > 0
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size <= 0:
            raise ValueError('size must be > 0')
        else:
            self.__size = size
            self.__size = size

        """ Validate and instantiate x with condition:
                ~ must be an integer
                ~ must be > 0
        """
        if type(x) != int:
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x
        
        
        """ Validate and instantiate y with condition:
                ~ must be an integer
        """
        if type(y) != int:
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y

    
    def area(self):
        """ Public method area that returns the  area
        value of rectangle
        """
        return super().area()
         

    def display(self):
        """ public method display that prints in stdout the
        Rectangle instance with the character #
        """
        super().display()

    def __str__(self):
        """ A function that overrides __str__ to specify
        how strings are rendered for class Square"""
        return ('[Square] ({}) {:d}/{:d} - {:d}'.format(self.__id, self.__x, self.__y, self.__size))

    def update(self):
        """Defines public method update that assigns an
        argument to each attribute in a positional order
        """
        super().update()

# s1 = Square(5)
# print(s1)
# print(s1.area())
# s1.display()

# print("---")

# s2 = Square(2, 2)
# print(s2)
# print(s2.area())
# s2.display()

# print("---")

# s3 = Square(3, 1, 3)
# print(s3)
# print(s3.area())
# s3.display()