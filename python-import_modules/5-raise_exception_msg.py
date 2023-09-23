def raise_exception_msg(message=""):
    raise NameError('{:s}'.format(message))

# try:
#     message = "C is fun"
#     raise_exception_msg(message)
# except NameError as ne:
#     print(ne)