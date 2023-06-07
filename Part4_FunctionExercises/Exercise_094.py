"""
Exercise 94: Random Password

    Write a function that generates a random password. The password should have a
    random length of between 7 and 10 characters. Each character should be randomly
    selected from positions 33 to 126 in the ASCII table. Your function will not take
    any parameters. It will return the randomly generated password as its only result.
    Display the randomly generated password in your file’s main program. Your main
    program should only run when your solution has not been imported into another file.
    Hint: You will probably find the chr function helpful when completing this
    exercise. Detailed information about this function is available online.
"""

# We need to import random library

import random


def generate_password():
    password_length = random.randint(7, 10)
    password = ""
    for _ in range(password_length):
        password += chr(random.randint(33, 126))
    return password


def main():
    password = generate_password()
    print("Randomly generated password:", password)


if __name__ == '__main__':
    main()
