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
        lst_arg = enumerate(args)
        if n == 1:
            #print('{:d} argument:\n{}: {}'.format(n, ((i, j) for i, j in lst_arg)))
            print("just wait")
        elif n == 0:
            print('{:d} arguments.'.format(n))
        else:
            #print('{:d} arguments:\n{}'.format(n, enumerate(args)))
            print('{:d} argument:\n{}: {}'.format(n, ((i, j) for i, j in lst_arg)))

list_arg(1, 2, "Hello", "Kwara")