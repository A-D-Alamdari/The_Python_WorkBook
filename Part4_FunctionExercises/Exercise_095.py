"""
Exercise 95: Random License Plate

    In a particular jurisdiction, older license plates consist of three letters followed by
    three numbers. When all of the license plates following that pattern had been used,
    the format was changed to four numbers followed by three letters.
    Write a function that generates a random license plate. Your function should have
    approximately equal odds of generating a sequence of characters for an old license
    plate or a new license plate. Write a main program that calls your function and
    displays the randomly generated license plate.
"""

# We need to import random library

import random
import string


def generate_license_plate():
    if random.random() < 0.5:
        # Generate an old license plate (three letters followed by three numbers)
        letters = ''.join(random.choices(string.ascii_uppercase, k=3))
        numbers = ''.join(random.choices(string.digits, k=3))
        license_plate = f"{letters}{numbers}"
    else:
        # Generate a new license plate (four numbers followed by three letters)
        numbers = ''.join(random.choices(string.digits, k=4))
        letters = ''.join(random.choices(string.ascii_uppercase, k=3))
        license_plate = f"{numbers}{letters}"

    return license_plate


def main():
    license_plate = generate_license_plate()
    print("Randomly generated license plate:", license_plate)


if __name__ == '__main__':
    main()
