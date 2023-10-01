""" This is a module that serves as the major
base for the rest of this project. It creates and 
initializes the class Base whose goal is to manage
id attribute in all future classes in this project,
"""
class Base:
    """ A class Base which will serve as the super class
    for all other classes in the AirBnB project
    """
    def __init__(self, id=None):
        """ Initializes the class Base with a keyword argument
        id. Set default value of __nb_objects to 0. 
        """
        __nb_objects = 0

        """If a value is given for id assign it to id, otherwise
        increment __nb_objects and assign its value to id
        """
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
            
        

# b = Base()
# if b is None:
#     print("Can't create Base")
#     exit(1)

# if b.id != 1:
#     print("ID is not equal to 1: {}".format(b.id))
#     exit(1)
    
# for i in range(2):
#     btmp = Base()

# btest = Base()
# if btest is None:
#     print("Can't create Base")
#     exit(1)

# if btest.id != 4:
#     print("ID is not equal to 4 after 3 other creations: {}".format(btest.id))
#     exit(1)

# print("OK", end="")
        