"""
Exercise 99:Arbitrary Base Conversions

    Write a program that allows the user to convert a number from one base to another.
    Your program should support bases between 2 and 16 for both the input number and
    the result number. If the user chooses a base outside of this range then an appropriate
    error message should be displayed and the program should exit. Divide your program
    into several functions, including a function that converts from an arbitrary base to
    base 10, a function that converts from base 10 to an arbitrary base, and a main
    program that reads the bases and input number from the user. You may find your
    solutions to Exercises 77, 78 and 98 helpful when completing this exercise.
"""


def convert_to_decimal(number, base):
    decimal = 0
    power = 0
    while number != 0:
        digit = number % 10
        if digit >= base:
            raise ValueError("Invalid digit '{}' for base {}".format(digit, base))
        decimal += digit * pow(base, power)
        number //= 10
        power += 1
    return decimal


def convert_from_decimal(decimal, base):
    result = ""
    while decimal != 0:
        digit = decimal % base
        result = str(digit) + result
        decimal //= base
    return result


def main():
    input_number = input("Enter the number to convert: ")
    input_base = int(input("Enter the base of the input number: "))
    output_base = int(input("Enter the base to convert to: "))

    if not (2 <= input_base <= 16) or not (2 <= output_base <= 16):
        print("Error: Base must be between 2 and 16")
        return

    try:
        decimal = convert_to_decimal(int(input_number), input_base)
        result = convert_from_decimal(decimal, output_base)
        print("Result:", result)
    except ValueError as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()
