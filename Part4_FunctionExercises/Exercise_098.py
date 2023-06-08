"""
Exercise 98: Hexadecimal and Decimal Digits

    Write two functions, hex2int and int2hex, that convert between hexadecimal
    digits (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E and F) and base 10 integers. The
    hex2int function is responsible for converting a string containing a single hexadec-
    imal digit to a base 10 integer, while the int2hex function is responsible for con-
    verting an integer between 0 and 15 to a single hexadecimal digit. Each function
    will take the value to convert as its only parameter and return the converted value
    as the function’s only result. Ensure that the hex2int function works correctly for
    both uppercase and lowercase letters. Your functions should end the program with a
    meaningful error message if an invalid parameter is provided.
"""


def hex2int(hex_digit):
    if len(hex_digit) != 1 or not hex_digit.isalnum() or hex_digit.isdigit() or not (
            hex_digit.isupper() or hex_digit.islower()):
        raise ValueError("Invalid hexadecimal digit: {}".format(hex_digit))

    hex_values = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }

    return hex_values[hex_digit.upper()]


def int2hex(integer):
    if not 0 <= integer <= 15:
        raise ValueError("Invalid integer: {}".format(integer))

    hex_values = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
        8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
    }

    return hex_values[integer]


# Example usage:
hex_digit = input("Enter a hexadecimal digit: ")
if len(hex_digit) != 1 or not hex_digit.isalnum() or hex_digit.isdigit() or not (
        hex_digit.isupper() or hex_digit.islower()):
    print("Error: Invalid hexadecimal digit")
else:
    decimal = hex2int(hex_digit)
    print("Decimal: {}".format(decimal))

integer = int(input("Enter an integer between 0 and 15: "))
if not 0 <= integer <= 15:
    print("Error: Invalid integer")
else:
    hex_digit = int2hex(integer)
    print("Hexadecimal: {}".format(hex_digit))

