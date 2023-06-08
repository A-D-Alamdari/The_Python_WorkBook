"""
Exercise 97: Random Good Password

    Using your solutions to Exercises 94 and 96, write a program that generates a random
    good password and displays it. Count and display the number of attempts that were
    needed before a good password was generated. Structure your solution so that it
    imports the functions you wrote previously and then calls them from a function
    named main in the file that you create for this exercise.
"""
from Part4_FunctionExercises.Exercise_094 import generate_password
from Part4_FunctionExercises.Exercise_096 import is_good_password


def main():
    attempts = 0
    password = generate_password()

    while not is_good_password(password):
        attempts += 1
        password = generate_password()

    print("Good password:", password)
    print("Attempts needed:", attempts)


if __name__ == "__main__":
    main()

