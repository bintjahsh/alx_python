""" This module contains the creation and initialization of a class
called 'Square'. Square will have the properties: size and area
- derived from size
"""
class Square:
    """Creation of class Square which will contain different attributes
    of a square in a private and protected capacity
    """
    def __init__(self, size=0):
        """initializing Square with a private instance attribute 'size'
        as the size of every square is unique and consequential
        """
        self.__size = size
        self.square_area = size**2

    def size(self):
        """Retrieve the size of the square as a
        public attribute
        """
        return self.__size

    def size(self, value):
        """Set square property 'size' to the value
        of 'value'
        """
        self.size = value
        
        """Size must be an integer, otherwise raise
        a TypeError
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            """Size must be greater than 0, otherwise
            raise a ValueError
            """
            raise ValueError('size must be >= 0')
        else:
            return value



    def area(self):
            """Return the current square area
            """
            return self.square_area