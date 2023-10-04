""" A class Square that inherits from Rectangle 
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """ A class Square that inherits from class Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize Rectangle with private instance attributes
        width, height, x and y
        """
        self.id = id
        
        super().__init__(size, size, x, y, id)
        self.x = x
        self.y = y
        

        if type(size) != int:
            """ Validate and instantiate size with condition:
                ~ must be an integer
                ~ must be > 0
            """
            raise TypeError('size must be an integer')
        elif size <= 0:
            raise ValueError('size must be > 0')
        else:
            self.width = size
            self.height = size

        
        if type(x) != int:
            """ Validate and instantiate x with condition:
                ~ must be an integer
                ~ must be > 0
            """
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x
        
        
        if type(y) != int:
            """ Validate and instantiate y with condition:
                ~ must be an integer
            """
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y


    @Rectangle.width.setter
    def size(self, size):
        """ Defines setter for public attribute size
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size <= 0:
            raise ValueError('size must be > 0')
        else:
            self.width = size
            self.height = size

            

    
    def area(self):
        """ Public method area that returns the  area
        value of rectangle
        """
        return super().area()
         

    def display(self):
        """ public method display that prints in stdout the
        Square instance with the character #
        """
        super().display()


    def __str__(self):
        """ A function that overrides __str__ to specify
        how strings are rendered for class Square"""
        super().__str__()
        return ('[Square] ({}) {:d}/{:d} - {:d}'.format(self.id, self.__x, self.__y, self.__size))

    def update(self, *args, **kwargs):
        """Defines public method update that assigns an
        argument to each attribute in a positional order
        """
        super().update()

# s = Square(12)
# if s is None:
#     print("Can't create Square")
#     exit(1)

# for attribute in list(s.__dict__.keys()):
#     if "size" in attribute:
#         print("You are not allowed to add any new attribute for size: {}".format(attribute))
#         exit(1)

# if s.size != 12:
#     print("Wrong size getter: {}".format(s.size))
#     exit(1)

# s.size = 5

# if s.size != 5:
#     print("Wrong size getter: {}".format(s.size))
#     exit(1)

# print("OK", end="")

       