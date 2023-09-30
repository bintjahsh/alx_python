""" Defines an empty class BaseGeometry
"""
class BaseGeometry:
    """ An empty class BaseGeometry
    """
    def _dir_(cls):

        """This is to exclude the init_subclass attribute 
        from printing
        """
        return [attribute for attribute in super()._dir() if attribute != '__init_subclass_']

# print(dir(BaseGeometry))
# print(BaseGeometry)