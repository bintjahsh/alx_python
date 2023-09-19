def count_arg(*args):
    n = len(args)
    if n == 1:
        return f'{n} argument):\n {args}'
    elif n == 0:
        return f'{n} arguments.'
    else:
        for arg in args[:]:
            return f'{n} arguments: \n {arg}'

print(count_arg(24, 5, "oruko", "jerry"))
#print(count_arg())