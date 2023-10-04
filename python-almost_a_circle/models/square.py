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
        super().__init__(size, size, x, y, id)
        

        
        """ Validate and instantiate size with condition:
            ~ must be an integer
            ~ must be > 0
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size <= 0:
            raise ValueError('size must be > 0')
        else:
            self.__size = size
            self.__size = size

        """ Validate and instantiate x with condition:
                ~ must be an integer
                ~ must be > 0
        """
        if type(x) != int:
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x
        
        
        """ Validate and instantiate y with condition:
                ~ must be an integer
        """
        if type(y) != int:
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y

    
    def area(self):
        """ Public method area that returns the  area
        value of rectangle
        """
        return super().area()
         

    def display(self):
        """ public method display that prints in stdout the
        Rectangle instance with the character #
        """
        super().display()

    def __str__(self):
        """ A function that overrides __str__ to specify
        how strings are rendered for class Square"""
        return ('[Square] ({}) {:d}/{:d} - {:d}'.format(self.__id, self.__x, self.__y, self.__size))

    def update(self):
        """Defines public method update that assigns an
        argument to each attribute in a positional order
        """
        super().update()

# s = Square(5, 7)
# if s.id != 1:
#     print("ID must be equal to 1: {}".format(s.id))
#     exit(1)

# if s.width != 5:
#     print("Width of the Square must be 5: {}".format(s.width))
#     exit(1)

# if s.height != 5:
#     print("Height of the Square must be 5: {}".format(s.height))
#     exit(1)

# if s.x != 7:
#     print("X of the Square must be 7: {}".format(s.x))
#     exit(1)

# try:
#     Square(5, "12")
#     print("TypeError exception not raised")
#     exit(1)
# except TypeError as e:
#     if str(e) != "x must be an integer":
#         print("Wrong exception message: {}".format(e))
#         exit(1)
# except Exception as e:
#     print("Wrong exception: [{}] {}".format(type(e), e))
#     exit(1)

# try:
#     Square(5, [13])
#     print("TypeError exception not raised")
#     exit(1)
# except TypeError as e:
#     if str(e) != "x must be an integer":
#         print("Wrong exception message: {}".format(e))
#         exit(1)
# except Exception as e:
#     print("Wrong exception: [{}] {}".format(type(e), e))
#     exit(1)

# try:
#     Square(5, 13.12)
#     print("TypeError exception not raised")
#     exit(1)
# except TypeError as e:
#     if str(e) != "x must be an integer":
#         print("Wrong exception message: {}".format(e))
#         exit(1)
# except Exception as e:
#     print("Wrong exception: [{}] {}".format(type(e), e))
#     exit(1)

# try:
#     Square(5, { 'id': 12 })
#     print("TypeError exception not raised")
#     exit(1)
# except TypeError as e:
#     if str(e) != "x must be an integer":
#         print("Wrong exception message: {}".format(e))
#         exit(1)
# except Exception as e:
#     print("Wrong exception: [{}] {}".format(type(e), e))
#     exit(1)

# try:
#     Square(5, -12)
#     print("ValueError exception not raised")
#     exit(1)
# except ValueError as e:
#     if str(e) != "x must be >= 0":
#         print("Wrong exception message: {}".format(e))
#         exit(1)
# except Exception as e:
#     print("Wrong exception: [{}] {}".format(type(e), e))
#     exit(1)

# try:
#     Square(5, -89)
#     print("ValueError exception not raised")
#     exit(1)
# except ValueError as e:
#     if str(e) != "x must be >= 0":
#         print("Wrong exception message: {}".format(e))
#         exit(1)
# except Exception as e:
#     print("Wrong exception: [{}] {}".format(type(e), e))
#     exit(1)

# try:
#     Square(5, -1)
#     print("ValueError exception not raised")
#     exit(1)
# except ValueError as e:
#     if str(e) != "x must be >= 0":
#         print("Wrong exception message: {}".format(e))
#         exit(1)
# except Exception as e:
#     print("Wrong exception: [{}] {}".format(type(e), e))
#     exit(1)

# try:
#     Square(5, 0)
#     print("OK", end="")
# except Exception as e:
#     print("0 is valid for x: [{}] {}".format(type(e), e))
#     exit(1)