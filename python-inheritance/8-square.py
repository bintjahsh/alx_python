""" Shape: this module is about a class Rectangle.
It inherits the attributes of base class BaseGeometry.
"""

Rectangle = __import__('7-rectangle').Rectangle

class Square(Rectangle):
    """ A class Square that inherits from Rectangle
    """
    def __init__(self, size):
        """ Instantiation with private instance property
        size
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ A function that calculates and returns the area of
         the Square"""
        area = self.__size ** 2
        return area
