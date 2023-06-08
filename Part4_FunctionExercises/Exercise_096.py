"""
Exercise 96: Check a Password

    In this exercise you will write a function that determines whether or not a password
    is good. We will define a good password to be a one that is at least 8 characters
    long and contains at least one uppercase letter, at least one lowercase letter, and at
    least one number. Your function should return true if the password passed to it as
    its only parameter is good. Otherwise it should return false. Include a main program
    that reads a password from the user and reports whether or not it is good. Ensure
    that your main program only runs when your solution has not been imported into
    another file.
"""


def is_good_password(password):
    # Check the length of the password
    if len(password) < 8:
        return False

    # Check if the password contains at least one uppercase letter, one lowercase letter, and one number
    has_uppercase = False
    has_lowercase = False
    has_number = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_number = True

        # Break the loop if all criteria are met
        if has_uppercase and has_lowercase and has_number:
            break

    # Return True if all criteria are met, otherwise False
    return has_uppercase and has_lowercase and has_number


def main():
    password = input("Enter a password: ")

    if is_good_password(password):
        print("Good password")
    else:
        print("Not a good password")


if __name__ == "__main__":
    main()
