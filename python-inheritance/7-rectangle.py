""" Shape: this module is about a class Rectangle.
It inherits the attributes of base class BaseGeometry.
"""

BaseGeometry = __import__('5-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ A class rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """ Instantiation with private instance properties
        width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height


    def __str__(self):
        """ A function that overrides __str__ to specify
        how strings are rendered for class Rectangle"""
        return ('[Rectangle] {:d}/{:d}'.format(self.__width, self.__height))

    def area(self):
        """ A function that calculates and returns the area of
         the Rectangle"""
        area = self.__width * self.__height
        return area