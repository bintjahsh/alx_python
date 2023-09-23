def safe_print_division(a, b):
    try:
        result = a / b
    except:
            result = 'None'
            return result
    finally:
        print('Inside result: {}'.format(result))
        return result


print(safe_print_division(2, 0))

