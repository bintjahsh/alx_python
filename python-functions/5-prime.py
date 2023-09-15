def is_prime(number):
    if number == 1:
        return False
    elif number > 1:
        for num in range(2, number):
            if (number % num) == 0:
                return False
                break
        else:
            return True
    else:
        return False
