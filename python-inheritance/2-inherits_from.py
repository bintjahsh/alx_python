""" A module that checks if an object
is an instance of a class that inherited
(directly or indirectly) from the specified class
"""
def inherits_from(obj, a_class):
    """ Returns true if obj is an instance of any
    of the subclasses of a_class and false otherwise
    """
    if type(obj) == a_class:
        return False
    else:
        return issubclass(type(obj), a_class)
    # print(isinstance(obj, a_class))
    # print(issubclass(type(obj), a_class))

# a = True
# print(inherits_from(a, object))
# should return True
# print(isinstance(True, object))
# a = 1
# print(inherits_from(a, int))
# should return false
# inherits_from(True, object)
# inherits_from(1, int)
# print(type(1))