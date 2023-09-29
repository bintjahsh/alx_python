""" A module that checks if an object
is an instance of a class that inherited
(directly or indirectly) from the specified class
"""
def inherits_from(obj, a_class):
    """ Returns true if obj is an instance of any
    of the subclasses of a_class and false otherwise
    """
    # return issubclass(type(obj), type(a_class).__bases__)
    if (type(obj) in a_class.__subclasses__()) | isinstance(obj, a_class):
        return True
    else:
        return False

# a = True
# print(inherits_from(a, int))
# a = True
# print(inherits_from(a, object))
# print(isinstance(True, object))