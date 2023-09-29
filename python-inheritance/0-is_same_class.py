""" A module that checks if an object is 
an instance of a specific class
"""
def is_same_class(obj, a_class):
    """ Returns true if obj is an instance of a_class
    and false otherwise
    """
    if type(obj) == type(a_class):
        return True
    else:
        return False

# a = 1
# if is_same_class(a, int):
#     print("{} is an instance of the class {}".format(a, int.__name__))
# if is_same_class(a, float):
#     print("{} is an instance of the class {}".format(a, float.__name__))
# if is_same_class(a, object):
#     print("{} is an instance of the class {}".format(a, object.__name__))