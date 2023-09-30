""" Defines a class BaseGeometry
"""
class BaseGeometry:
    """ A base class for geometry formation
    """
    def area(self):
        """ A function area that raises a custom
        exception when called
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ A function that validates value and raises a
        TypeError if value is not an integer and a ValueError
        if value is <= 0
        """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))