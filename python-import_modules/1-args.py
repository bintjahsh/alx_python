import sys

if __name__ == "__main__":
    #def count_arg(*argv):
        n = len(sys.argv)
        if n == 1:
            print('{:d} argument:\n{:s}'.format(n, sys.argv[0:].enumerate()))
        elif n == 0:
            print('{:d} arguments.'.format(n))
        else:
                print('{:d} arguments:\n{:s}'.format(*sys.argv[0:].enumerate(), sep='\n'))

#count_arg(24, 5, "oruko", "jerry")