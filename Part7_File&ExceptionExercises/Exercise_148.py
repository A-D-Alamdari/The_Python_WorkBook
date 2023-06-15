"""
Exercise 148:Sum a List of Numbers

    Create a program that sums all of the numbers entered by the user while ignoring
    any lines entered by the user that are not valid numbers. Your program should dis-
    play the current sum after each number is entered. It should display an appropriate
    error message after any invalid input, and then continue to sum any additional num-
    bers entered by the user. Your program should exit when the user enters a blank
    line. Ensure that your program works correctly for both integers and floating point
    numbers.
    Hint: This exercise requires you to use exceptions without using files.
"""


def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def is_valid_number(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False


numbers = []
while True:
    user_input = input("Enter a number (blank to exit): ")
    if user_input == "":
        break

    if is_valid_number(user_input):
        number = float(user_input)
        numbers.append(number)
        current_sum = calculate_sum(numbers)
        print("Current sum:", current_sum)
    else:
        print("Invalid input. Please enter a valid number.")

print("Final sum:", calculate_sum(numbers))
