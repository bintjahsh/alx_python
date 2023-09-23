import sys

if __name__ == "__main__":
        # n = len(sys.argv)
        # if n == 1:
        #     print('{:d} argument:\n{}'.format(n, sys.argv[0]))
        # elif n <= 1:
        #     print('{:d} arguments.'.format(n))
        # else:
        #         print('{:d} arguments:\n{:d}: {}'.format(n, 'i, j in enumerate(*sys.argv[1:])', sep='\n'))
    def list_arg(*args):
        n = len(args)
        lst_arg = []
        if n == 1:
            print('{:d} argument:'.format(n))
            for i, arg in enumerate(list(args)):
                print(('{}: {}'.format(i, arg)))
        elif n == 0:
            print('{:d} arguments.'.format(n))
        else:
            print('{:d} arguments:'.format(n))
            for i, arg in enumerate(list(args)):
                print(('{}: {}'.format(i, arg)))

# list_arg(1, 5, "Hello", "Kwara")
# list_arg("hello")