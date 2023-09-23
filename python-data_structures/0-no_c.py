def no_c(my_string):
    newString = [x for x in list(my_string) if x != 'c']
    my_string = [x for x in list(newString) if x != 'C']
    newString = "".join(my_string)
    return newString

# word = "School"
# new_word = no_c(word)

# print(new_word)
# print(word)