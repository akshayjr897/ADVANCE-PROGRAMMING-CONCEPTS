
#  password strngth

import re

def check_password(password):

    
    if len(password) < 8:
        return False

    
    if not re.search(r'[A-Z]', password):
        return False

    
    if not re.search(r'[a-z]', password):
        return False

    
    if not re.search(r'[0-9]', password):
        return False

   
    if not re.search(r'[!@#$%^&*()_-]', password):
        return False

    return True



password = input("Enter your password: ")


if check_password(password):
    print("Strong Password")
else:
    print("Weak Password")