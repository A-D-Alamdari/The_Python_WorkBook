"""
Exercise 142: Display the Tail of a File

    Unix-based operating systems also typically include a tool named tail. It displays
    the last 10 lines of a file whose name is provided as a command line parameter.
    Write a Python program that provides the same behavior. Display an appropriate
    error message if the file requested by the user does not exist or if the command line
    parameter is omitted.
    There are several different approaches that can be taken to solve this problem.
    One option is to load the entire contents of the file into a list and then display the
    last 10 elements. Another option is to read the contents of the file twice, once to
    count the lines, and a second time to display the last 10 lines. However, both of these
    solutions are undesirable when working with large files. Another solution exists that
    only requires you to read the file once, and only requires you to store 10 lines from
    the file at one time. For an added challenge, develop such a solution.
"""

import sys

NUM_LINES = 10

if len(sys.argv) != 2:
    print("You must provide the file name as a command line parameter!")
    quit()

try:
    filename = sys.argv[1]
    with open(filename, "r") as file:
        lines = []
        for line in file:
            lines.append(line.strip())
            if len(lines) > NUM_LINES:
                lines.pop(0)

        if len(lines) < NUM_LINES:
            print("The file contains fewer than 10 lines:")
        print("\n".join(lines))

except FileNotFoundError:
    print("The file requested does not exist!")
except IOError:
    print("An error occurred while accessing the file!")
