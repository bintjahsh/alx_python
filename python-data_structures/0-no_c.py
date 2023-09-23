def no_c(my_string):
    list(my_string).remove('c')
    newString = my_string
    list(newString).remove('C')
    my_string = newString