""" A module that checks if an object is an instance of,
or an instance of a class
that inherited from, the specified class 
"""
def is_kind_of_class(obj, a_class):
    """ Returns true if obj is an instance of a_class
    or any of its subclasses and false otherwise
    """
    return isinstance(obj, a_class)