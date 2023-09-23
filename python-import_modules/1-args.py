import sys

if __name__ == "__main__":
# def list_arg(*argv):
    n = len(sys.argv) - 1
    if n == 1:
        print('{:d} argument:'.format(n))
        for i, arg in enumerate(list(sys.argv[1:]), 1):
            print(('{}: {}'.format(i, arg)))
    elif n == 0:
        print('{:d} arguments.'.format(n))
    else:
        print('{:d} arguments:'.format(n))
        for i, arg in enumerate(list(sys.argv[1:]), 1):
            print(('{}: {}'.format(i, arg)))

# list_arg(1, 5, "Hello", "Kwara")
# list_arg("Hello")