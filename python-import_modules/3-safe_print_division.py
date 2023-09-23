def safe_print_division(a, b):
    try:
        result = a / b
    except:
            result = 'None'
            return result
    finally:
        # print('Inside result: {}'.format(result))
        return result

# a = 10
# b = 2
# result = safe_print_division(a, b)
# print("{:d} / {:d} = {}".format(a, b, result))

