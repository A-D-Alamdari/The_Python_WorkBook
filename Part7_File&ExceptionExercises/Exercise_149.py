"""
Exercise 149: Both Letter Grades and Grade Points

    Write a program that converts from letter grades to grade points and vice-versa.
    Your program will convert multiple values entered by the user, with one value
    entered on each line. Begin by attempting to convert each value entered by the
    user from a number of grade points to a letter grade. If an exception occurs dur-
    ing the attempt then your program should attempt to convert the value from a let-
    ter grade to a number of grade points. If both conversions fail then your program
    should provide a message indicating that the supplied input is invalid. Design your
    program so that it continues performing conversions until the user enters a blank
    line. Your solutions to Exercises 51 and 52 may be helpful when completing this
    exercise.
"""


def convert_to_grade_point(letter_grade):
    grade_point = None
    try:
        letter_grade = letter_grade.upper()
        grade_point = {
            'A+': 4.0,
            'A': 4.0,
            'A-': 3.7,
            'B+': 3.3,
            'B': 3.0,
            'B-': 2.7,
            'C+': 2.3,
            'C': 2.0,
            'C-': 1.7,
            'D+': 1.3,
            'D': 1.0,
            'F': 0.0
        }[letter_grade]
    except KeyError:
        pass
    return grade_point


def convert_to_letter_grade(grade_point):
    letter_grade = None
    try:
        grade_point = float(grade_point)
        if grade_point == 4.0:
            letter_grade = 'A'
        elif grade_point >= 3.7:
            letter_grade = 'A-'
        elif grade_point >= 3.3:
            letter_grade = 'B+'
        elif grade_point >= 3.0:
            letter_grade = 'B'
        elif grade_point >= 2.7:
            letter_grade = 'B-'
        elif grade_point >= 2.3:
            letter_grade = 'C+'
        elif grade_point >= 2.0:
            letter_grade = 'C'
        elif grade_point >= 1.7:
            letter_grade = 'C-'
        elif grade_point >= 1.3:
            letter_grade = 'D+'
        elif grade_point >= 1.0:
            letter_grade = 'D'
        elif grade_point < 1.0:
            letter_grade = 'F'
    except ValueError:
        pass
    return letter_grade


while True:
    user_input = input("Enter a grade point or letter grade (blank to exit): ")
    if user_input == "":
        break

    grade_point = convert_to_grade_point(user_input)
    letter_grade = convert_to_letter_grade(user_input)

    if grade_point is not None:
        print("Grade point equivalent:", grade_point)
    elif letter_grade is not None:
        print("Letter grade equivalent:", letter_grade)
    else:
        print("Invalid input. Please enter a valid grade point or letter grade.")
