""" A class Rectangle that inherits from Base 
"""
from base import Base

class Rectangle(Base):
    """ A class Rectangle that inherits from super class Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize Rectangle with private instance attributes
        width, height, x and y
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.y = y
        self.id = Base.id
    
    @property
    def width(self):
        """ Defines public getter for attribute width
        """
        self.width = self.__width

    @width.setter
    def width(self, width):
        """ Defines public setter for attribute width
        """
        self.width = width

    @property
    def height(self):
        """ Defines public getter for attribute width
        """
        self.height = self.__height

    @height.setter
    def height(self, height):
        """ Defines public setter for attribute width
        """
        self.height = height
    
    @property
    def x(self):
        """ Defines public getter for attribute width
        """
        self.x = self.__x

    @x.setter
    def height(self, x):
        """ Defines public setter for attribute width
        """
        self.x = x

    @property
    def y(self):
        """ Defines public getter for attribute width
        """
        self.y = self.__y

    @y.setter
    def height(self, y):
        """ Defines public setter for attribute width
        """
        self.y = y