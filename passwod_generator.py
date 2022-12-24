import random

MAX_PWDS = 10
MIN_PWDS = 1
MAX_PWD_LENGTH = 10
MIN_PWD_LENGTH = 4
NUM_PWDS = 0
PWD_LENGTH = 0

print("Welcome to the password Generator")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*().,;:'

#Gather number of passwords
def numPWDS():
    while True:
        number = input(f"Number of passwords to generate ({MIN_PWDS}-{MAX_PWDS}): ")
        if number.isdigit():
            number = int(number)
            if MIN_PWDS <= number <= MAX_PWDS:
                return(number)
            else:
                print("Please try again.")
        else:
            print("Please enter a number value")

#Gather password Length
def pwdLength():
    while True:
        length = input(f"Length of password(s) ({MIN_PWD_LENGTH}-{MAX_PWD_LENGTH}): ")
        if length.isdigit():
            length = int(length)
            if MIN_PWD_LENGTH <= length <= MAX_PWD_LENGTH:
                return(length)
            else:
                print("Please try again.")
        else:
            print("Please enter a number value")


#Print results
def printPWDS():
    print("Here are your passwords:")
    for _ in range(NUM_PWDS):
        password = ""
        for _ in range(PWD_LENGTH):
            password += random.choice(chars)
        print (password)

#Call and run programs
NUM_PWDS = numPWDS()
PWD_LENGTH = pwdLength()
printPWDS()