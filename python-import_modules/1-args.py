import sys

if __name__ == "__main__":
        n = len(sys.argv)
        if n == 1:
            print('{:d} argument:\n{}'.format(n, sys.argv[0]))
        elif n <= 1:
            print('{:d} arguments.'.format(n))
        else:
                print('{:d} arguments:\n{:d}: {}'.format(n, 'i, j in enumerate(*sys.argv[1:])', sep='\n'))
