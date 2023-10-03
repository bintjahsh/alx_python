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
    
        # if id != None:
        #     """If a value is given for id assign it to id, otherwise
        #     increment __nb_objects and assign its value to id
        #     """
        #     self.id = id
        #     Rectangle.__nb_objects += id
        # else:
        #     Rectangle.__nb_objects += 1
        
        #     self.id = Rectangle.__nb_objects
    
    @property
    def width(self):
        """ Defines public getter for attribute width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """ Defines public setter for attribute width
        """
        self.__width = width

    @property
    def height(self):
        """ Defines getter for public attribute height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """ Defines setter for public attribute height
        """
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
        self.__y = y


# r = Rectangle(12, 14, 4, 5, 10)
# if r is None:
#     print("Can't create Rectangle")
#     exit(1)

# if r._Rectangle__height != 14:
#     print("Wrong private height: {}".format(r._Rectangle__height))
#     exit(1)

# if r.height != 14:
#     print("Wrong height getter: {}".format(r.height))
#     exit(1)

# r.height = 7

# if r._Rectangle__height != 7:
#     print("Wrong private height: {}".format(r._Rectangle__height))
#     exit(1)

# if r.height != 7:
#     print("Wrong height getter: {}".format(r._Rectangle__height))
#     exit(1)

# print("OK", end="")