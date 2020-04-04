import random
import string

user = {}
def getUserInput():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email address: ")
    randoms = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(5)])
    password = first_name[:2] + last_name[-2:] + randoms
    print(password)
    while True:   
        satisfied = input("Are you satisfied with the password shown(y/n): ").lower()
        if satisfied == 'y':
            details = {first_name:{'firstname': first_name, 'lastname': last_name, 'email': email, 'password': password}}
            user.update(details)
            print(user[first_name])
            print(user)
            newUser = input("Another user(y/n): ").lower()
            if newUser == "y":
                getUserInput()
            elif newUser == "n":
                break
        else:
            while True:
                password = input("Enter your preferred password: ")
                if len(password) < 7:
                    print("password must be greater than 7 characters")
                    continue
                else:
                    details = {first_name:{'firstname': first_name, 'lastname': last_name, 'email': email, 'password': password}}
                    user.update(details)
                    print(user[first_name])
                    print(user)
                    newUser = input("Another user(y/n): ").lower()
                    if newUser == "y":
                        getUserInput()
                    elif newUser == "n":
                        break


getUserInput()