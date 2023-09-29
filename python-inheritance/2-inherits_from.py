""" A module that checks if an object
is an instance of a class that inherited
(directly or indirectly) from the specified class
"""
def inherits_from(obj, a_class):
    """ Returns true if obj is an instance of any
    of the subclasses of a_class and false otherwise
    """
    return issubclass(type(obj), a_class)

# a = True
# print(inherits_from(a, int))
