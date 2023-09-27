""" This module contains the creation and initialization of a class
called 'Square'. 
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
        
        """ Size must be an integer, otherwise raise
        a TypeError
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')

        """ Size must be greater than 0, otherwise
        raise a ValueError
        """
        if size < 0:
            raise ValueError('size must be >= 0')


    
    