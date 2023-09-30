""" Defines a class BaseGeometry
"""
class BaseGeometry:
    """ Initializes the class BaseGeometry
    """
    # def _dir_(cls):

    #     """This is to exclude the init_subclass attribute 
    #     from printing
    #     """
    #     return [attribute for attribute in super()._dir() if attribute != '__init_subclass_']


    def area(self):
        """ A function area that raises a custom
        exception when called
        """
        raise Exception('area() is not implemented')

# bg = BaseGeometry()

# try:
#     print(bg.area())
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

