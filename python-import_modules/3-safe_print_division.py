def safe_print_division(a, b):
    try:
        result = a / b
    except:
            result = 'None'
    finally:
        print('Inside result: {} \n {:d} / {:d} = {}'.format(result, a, b, result))


print(safe_print_division(4, 2))

