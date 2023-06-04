"""
Exercise 52: Grade Points to Letter Grade

    In the previous exercise you created a program that converts a letter grade into the
    equivalent number of grade points. In this exercise you will create a program that
    reverses the process and converts from a grade point value entered by the user to a
    letter grade. Ensure that your program handles grade point values that fall between
    letter grades. These should be rounded to the closest letter grade. Your program
    should report A+ for a 4.0 (or greater) grade point average.
"""

# Get input from user
grade_point = float(input("Enter the grade point: "))

# Determine the letter grade
if grade_point >= 4.0:
    letter_grade = "A+"
elif 3.7 <= grade_point < 4.0:
    letter_grade = "A"
elif 3.3 <= grade_point < 3.7:
    letter_grade = "A-"
elif 3.0 <= grade_point < 3.3:
    letter_grade = "B+"
elif 2.7 <= grade_point < 3.0:
    letter_grade = "B"
elif 2.3 <= grade_point < 2.7:
    letter_grade = "B-"
elif 2.0 <= grade_point < 2.3:
    letter_grade = "C+"
elif 1.7 <= grade_point < 2.0:
    letter_grade = "C"
elif 1.3 <= grade_point < 1.7:
    letter_grade = "C-"
elif 1.0 <= grade_point < 1.3:
    letter_grade = "D+"
elif 0.7 <= grade_point < 1.0:
    letter_grade = "D"
elif 0.0 <= grade_point < 0.7:
    letter_grade = "F"
else:
    letter_grade = ""


# Display the result
if letter_grade == "":
    print("You entered an INVALID input!")
else:
    print(f"The grade point {grade_point} is equivalent to the letter grade {letter_grade}.")

