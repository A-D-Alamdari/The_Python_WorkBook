"""
Exercise 51: Letter Grade to Grade Points

    At a particular university, letter grades are mapped to grade points in the following
    manner:
                Letter      Grade points
                ------------------------
                A+          4.0
                A           4.0
                A−          3.7
                B+          3.3
                B           3.0
                B−          2.7
                C+          2.3
                C           2.0
                C−          1.7
                D+          1.3
                D           1.0
                F           0
    Write a program that begins by reading a letter grade from the user. Then your
    program should compute and display the equivalent number of grade points. Ensure
    that your program generates an appropriate error message if the user enters an invalid
    letter grade.
"""

A       = 4.0
A_MINUS = 3.7
B_PLUS  = 3.3
B       = 3.0
B_MINUS = 2.7
C_PLUS  = 2.3
C       = 2.0
C_MINUS = 1.7
D_PLUS  = 1.3
D       = 1.0
F       = 0
INVALID = -1


# READ THE LETTER GRADES FROM THE USER
letter = input("Enter a letter grade: ")

# The statement "letter = letter.upper()" converts amy lowercase letters entered by the user into
# uppercase letters, storing the result back into the same variable. Including this statement allows
# the program to work with lowercase letters without including them in the conditions of the IF-Statements.
letter = letter.upper()

gp = None
if letter == "A+" or letter == "A":
    gp = A
elif letter == "A-":
    gp = A_MINUS
elif letter == "B+":
    gp = B_PLUS
elif letter == "B":
    gp = B
elif letter == "B-":
    gp = B_MINUS
elif letter == "C+":
    gp = C_PLUS
elif letter == "C":
    gp = C
elif letter == "C-":
    gp = C_MINUS
elif letter == "D+":
    gp = D_PLUS
elif letter == "D":
    gp = D
elif letter == "F":
    gp = F
else:
    gp = INVALID


# Display the output
if gp == INVALID:
    print("Invalid input.")
else:
    print(f"That's {gp} grade points.")
