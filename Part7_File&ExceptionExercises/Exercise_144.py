"""
Exercise 144: Number the Lines in a File

    Create a program that adds line numbers to a file. The name of the input file will be
    read from the user, as will the name of the new file that your program will create.
    Each line in the output file should begin with the line number, followed by a colon
    and a space, followed by the line from the input file.
"""

input_file = input("Enter the name of the input file: ")
output_file = input("Enter the name of the output file: ")

try:
    with open(input_file, "r") as file:
        lines = file.readlines()

    with open(output_file, "w") as file:
        for i, line in enumerate(lines, 1):
            file.write(f"{i}: {line}")

    print("Line numbers added successfully!")

except FileNotFoundError:
    print("The input file does not exist!")
except IOError:
    print("An error occurred while accessing the file!")
