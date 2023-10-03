""" A class Rectangle that inherits from Base 
"""
from models.base import Base

class Rectangle(Base):
    """ A class Rectangle that inherits from super class Base
    """
    # __nb_objects = 0
    """ Set default value of private attribute __nb_objects to 0.
    """

    def __init__(self, width=0, height=0, x=0, y=0, id=None):
        """ Initialize Rectangle with private instance attributes
        width, height, x and y
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    
    @property
    def width(self):
        """ Defines public getter for attribute width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """ Defines setter for public attribute width
        """
        if type(width) != int:
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width


    @property
    def height(self):
        """ Defines getter for public attribute height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """ Defines setter for public attribute height with conditions:
                ~ must be an integer
                ~ must be > 0
        """
        if type(height) != int:
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height
    
    @property
    def x(self):
        """ Defines public getter for attribute x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """ Defines public setter for attribute x
        """
        if type(x) != int:
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x

    @property
    def y(self):
        """ Defines public getter for attribute y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """ Defines public setter for attribute y
        """
        if type(y) != int:
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y