def is_same_class(obj, a_class):
    """ To check if an object is an instance of 
    a specific class
    """
    if isinstance(obj, a_class):
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