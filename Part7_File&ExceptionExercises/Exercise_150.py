"""
Exercise 150:Remove Comments

    Python uses the # character to mark the beginning of a comment. The comment ends
    at the end of the line containing the # character. In this exercise, you will create a
    program that removes all of the comments from a Python source file. Check each
    line in the file to determine if a # character is present. If it is then your program
    should remove all of the characters from the # character to the end of the line (we’ll
    ignore the situation where the comment character occurs inside of a string). Save the
    modified file using a new name that will be entered by the user. The user will also
    enter the name of the input file. Ensure that an appropriate error message is displayed
    if a problem is encountered while accessing the files.
"""


def remove_comments(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()

        with open(output_file, 'w') as file:
            for line in lines:
                line = line.split('#', 1)[0]  # Remove comment starting from #
                file.write(line)

        print("Comments removed successfully. Modified file saved as", output_file)

    except FileNotFoundError:
        print("Input file not found.")
    except IOError:
        print("An error occurred while accessing the file.")


input_file = input("Enter the name of the input file: ")
output_file = input("Enter the name of the output file: ")

remove_comments(input_file, output_file)
