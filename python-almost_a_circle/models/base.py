""" This is a module that serves as the major
base for the rest of this project. It creates and 
initializes the class Base whose goal is to manage
id attribute in all future classes in this project,
"""
class Base:
    """ A class Base which will serve as the super class
    for all other classes in the AirBnB project
    """
    __nb_objects = 0
    """ Set default value of private attribute __nb_objects to 0.
    """

    def __init__(self, id=None):
        """ Initializes the class Base with a keyword argument
        id.  
        """

        if id != None:
            """If a value is given for id assign it to id, otherwise
            increment __nb_objects and assign its value to id
            """
            self.id = id
            Base.__nb_objects += id
        else:
            Base.__nb_objects += 1
        
            self.id = Base.__nb_objects
