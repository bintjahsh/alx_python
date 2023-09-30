""" Defines a class BaseGeometry
"""
class BaseGeometry:
    """ Initializes the class BaseGeometry
    """
    def area(self):
        """ A function area that raises a custom
        exception when called
        """
        raise Exception('area() is not implemented')

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

