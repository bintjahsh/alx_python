def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
            result = 'None'
            return result
    finally:
        return ('Inside result: {} \n{:d} / {:d} = {}'.format(result, a, b, result))

#print(safe_print_division(a, b))

