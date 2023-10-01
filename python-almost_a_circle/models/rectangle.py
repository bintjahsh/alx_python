""" A class Rectangle that inherits from Base 
"""
from models.base import Base

class Rectangle(Base):
    """ A class Rectangle that inherits from super class Base
    """
    Base.__nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize Rectangle with private instance attributes
        width, height, x and y
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.id = Base.__nb_objects
    
        if id != None:
            """If a value is given for id assign it to id, otherwise
            increment __nb_objects and assign its value to id
            """
            self.id = id
            Base.__nb_objects += id
        else:
            Base.__nb_objects += 1
        
            self.id = Base.__nb_objects
    
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

# r = Rectangle(12, 14)
# if r is None:
#     print("Can't create Rectangle")
#     exit(1)

# if r._Rectangle__width != 12:
#     print("Wrong width: {}".format(r._Rectangle__width))
#     exit(1)

# if r._Rectangle__height != 14:
#     print("Wrong height: {}".format(r._Rectangle__height))
#     exit(1)

# if r._Rectangle__x != 0:
#     print("Wrong x: {}".format(r._Rectangle__x))
#     exit(1)

# if r._Rectangle__y != 0:
#     print("Wrong y: {}".format(r._Rectangle__y))
#     exit(1)

# if r.id != 1:
#     print("ID is not initialized at 1")
#     exit(1)

# print("OK", end="")