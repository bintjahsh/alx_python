def validate_password(password):
    count = 0
    while count < len(password):
        if  len(password) >= 8 & count >= 4:
            for a in password:
                if a.isupper() == True:
                        count += 1
                elif a.islower() == True:
                        count += 1
                elif a.isdigit() == True:
                        count += 1
                elif a.isspace() == True:
                        count += 1
                else:
                        return False
        return True

#print(validate_password("abc123"))

