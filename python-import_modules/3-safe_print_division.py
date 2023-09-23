def safe_print_division(a, b):
    try:
        result = a / b
    except:
            result = 'None'
            return result
    finally:
        return ('Inside result: {}'.format(result))

# print(safe_print_division(2, 0))

