""" This module contains the creation and initialization of a class
called 'Square'
"""
class Square:
    """Creation of class Square which will contain different attributes
    of a square in a private and protected capacity
    """
    def __init__(self, size):
        """initializing Square with a private instance attribute 'size'
        as the size of every square is unique and consequential
        """
        self.__size = size