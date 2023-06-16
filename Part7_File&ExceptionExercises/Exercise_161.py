"""
Exercise 161:Missing Comments

    When one writes a function, it is generally a good idea to include a comment that
    outlines the function’s purpose, its parameters and its return value. However, some-
    times comments are forgotten, or left out by well-intentioned programmers that plan
    to write them later but then never get around to it.
    Create a python program that reads one or more Python source files and identifies
    functions that are not immediately preceded by a comment. For the purposes of this
    exercise, assume that any line that begins with def, followed by a space, is the
    beginning of a function definition. Assume that the comment character, #, will be
    the first character on the previous line when the function has a comment. Display the
    names of all of the functions that are missing comments, along with the file name
    and line number where the function definition is located.
    The user will provide the names of one or more Python files as command line
    parameters. If your program encounters a file that doesn’t exist or can’t be opened
    then it should display an appropriate error message before moving on and processing
    the remaining files.
"""

import sys


def find_missing_comments(files):
    for file_name in files:
        try:
            with open(file_name, 'r') as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    if line.startswith('def ') and (i == 0 or not lines[i - 1].strip().startswith('#')):
                        function_name = line.split(' ')[1].split('(')[0]
                        print(f"Missing comment for function '{function_name}' in file '{file_name}', line {i + 1}")
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
        except IOError:
            print(f"Error reading file '{file_name}'.")


# Check if file names are provided as command line arguments
if len(sys.argv) < 2:
    print("Please provide one or more file names as command line parameters.")
else:
    # Get the file names from the command line arguments
    file_names = sys.argv[1:]
    find_missing_comments(file_names)
