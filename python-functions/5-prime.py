def is_prime(number):
    if number == 1:
        return False
    elif number > 1:
        for num in range(2, number):
            if (number % num) == 0:
                return False
        else:
            return True
    else:
        return False

print(is_prime(0))