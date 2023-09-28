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
        self.size = size
        self.square_area = size**2

    @property
    def size(self):
        """Retrieve the size of the square as a
        public attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
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
            """Set square property 'size' to the value
            of 'value'
            """
            self.__size = value

        self.square_area = value**2

    def area(self):
            """Return the current square area
            """
            return self.square_area

    def my_print(self):
        if self.size == 0:
            print('')
        else:
            myShape = []
            myShape_matrix = []
            for i in range(self.size):
                myShape.append(myShape_matrix)
            for j in range(self.size):
                myShape_matrix.append("#")
            
            for i in myShape:
                rowMatrix = ""
                for j in i:
                    rowMatrix += ('{:s}'.format(j))      
                print(rowMatrix)    

            # print(len(myShape))

            # print(len(myShape_matrix))
            

# my_square = Square(3)
# my_square.my_print()

# print("--")

# my_square.size = 6
# my_square.my_print()

# print("--")

# my_square.size = 0
# my_square.my_print()

# print("--")