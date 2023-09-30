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


# r = Rectangle(3, 5)

# print(r)

# try:
#     print("Rectangle: {} - {}".format(r.width, r.height))
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

# try:
#     r2 = Rectangle(4, True)
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))
