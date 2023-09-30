""" Imports base class BaseGeometry
"""
BaseGeometry = import('5-base_geometry').BaseGeometry

""" Creates a class Rectangle that inherits the attributes of 
base class BaseGeometry
"""

class Rectangle(BaseGeometry):
    """ A class rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """ Instantiation with private instance properties
        width and height
        """
        self.__width = width
        self.__height = height

        width.integer_validator()
        height.integer_validator()

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
