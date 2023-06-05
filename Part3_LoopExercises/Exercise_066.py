"""
Exercise 66: Compute a Grade Point Average

    Exercise 51 included a table that shows the conversion from letter grades to grade
    points at a particular academic institution. In this exercise you will compute the
    grade point average of an arbitrary number of letter grades entered by the user. The
    user will enter a blank line to indicate that all of the grades have been provided. For
    example, if the user enters A, followed by C+, followed by B, followed by a blank
    line then your program should report a grade point average of 3.1.
    You may find your solution to Exercise 51 helpful when completing this exercise.
    Your program does not need to do any error checking. It can assume that each value
    entered by the user will always be a valid letter grade or a blank line.
"""

A = 4.0
A_MINUS = 3.7
B_PLUS = 3.3
B = 3.0
B_MINUS = 2.7
C_PLUS = 2.3
C = 2.0
C_MINUS = 1.7
D_PLUS = 1.3
D = 1.0
F = 0

# initialize variables
total_grade_points = 0
count = 0

# Get input from user
while True:
    letter = input("Enter a letter grade (or leave blank to calculate GPA): ")

    if letter == "":
        break

    letter = letter.upper()

    if letter == "A+":
        grade_point = A
    elif letter == "A":
        grade_point = A
    elif letter == "A-":
        grade_point = A_MINUS
    elif letter == "B+":
        grade_point = B_PLUS
    elif letter == "B":
        grade_point = B
    elif letter == "B-":
        grade_point = B_MINUS
    elif letter == "C+":
        grade_point = C_PLUS
    elif letter == "C":
        grade_point = C
    elif letter == "C-":
        grade_point = C_MINUS
    elif letter == "D+":
        grade_point = D_PLUS
    elif letter == "D":
        grade_point = D
    elif letter == "F":
        grade_point = F
    else:
        print("Invalid letter grade.")
        continue

    total_grade_points += grade_point
    count += 1

# Compute average and display the result
if count == 0:
    print("No grades entered.")
else:
    gpa = total_grade_points / count
    print("GPA:", round(gpa, 1))

