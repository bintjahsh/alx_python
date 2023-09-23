def safe_print_division(a, b):
    try:
        result = a / b
    except:
            result = 'None'
            return result
    finally:
        # value = 'Inside result: {}\n{} / {} = {}'.format(result, a, b, result)
        return result

# print(safe_print_division(0, 2))

