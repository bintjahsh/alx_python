""" A class Rectangle that inherits from Base 
"""
from base import Base

class Rectangle(Base):
    """ A class Rectangle that inherits from super class Base
    """
    # __nb_objects = 0
    """ Set default value of private attribute __nb_objects to 0.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize Rectangle with private instance attributes
        width, height, x and y
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        # self.id = Base(id) 
        # self.id = Rectangle.__nb_objects
    
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
        # self.width = self.__width
        return self.__width

    @width.setter
    def width(self, width):
        """ Defines public setter for attribute width
        """
        self.__width = width

    @property
    def height(self):
        """ Defines public getter for attribute width
        """
        return self.__height

    @height.setter
    def height(self, height):
        """ Defines public setter for attribute width
        """
        self.__height = height
    
    @property
    def x(self):
        """ Defines public getter for attribute width
        """
        return self.__x

    @x.setter
    def height(self, x):
        """ Defines public setter for attribute width
        """
        self.__x = x

    @property
    def y(self):
        """ Defines public getter for attribute width
        """
        return self.__y

    @y.setter
    def height(self, y):
        """ Defines public setter for attribute width
        """
        self.__y = y


# r = Rectangle(12, 14, 4, 5, 10)
# if r is None:
#     print("Can't create Rectangle")
#     exit(1)

# if r._Rectangle__width != 12:
#     print("Wrong private width: {}".format(r._Rectangle__width))
#     exit(1)

# if r.width != 12:
#     print("Wrong width getter: {}".format(r._Rectangle__width))
#     exit(1)

# r.width = 5

# if r._Rectangle__width != 5:
#     print("Wrong private width: {}".format(r._Rectangle__width))
#     exit(1)

# if r.width != 5:
#     print("Wrong width getter: {}".format(r._Rectangle__width))
#     exit(1)

# print("OK", end="")