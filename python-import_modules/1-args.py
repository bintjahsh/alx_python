import sys

if __name__ == "__main__":
    #def count_arg(*argv):
        n = len(sys.argv)
        if n == 1:
            print('{:d} argument:\n{:s}'.format(n, enumerate(sys.argv[0:])))
        elif n == 0:
            print('{:d} arguments.'.format(n))
        else:
                print('{:d} arguments:\n{:s}'.format(enumerate(*sys.argv[0:]), sep='\n'))

#count_arg(24, 5, "oruko", "jerry")