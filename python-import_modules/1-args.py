import sys

if __name__ == "__main__":
    #def count_arg(*argv):
        n = len(sys.argv)
        if n == 1:
            print('{:d} argument:\n{:s}'.format(n, sys.argv[1]))
        elif n == 0:
            print('{:d} arguments.'.format(n-1))
        else:
                print('{:d} arguments:\n{:s}'.format(*sys.argv[1:], sep='\n'))

#count_arg(24, 5, "oruko", "jerry")