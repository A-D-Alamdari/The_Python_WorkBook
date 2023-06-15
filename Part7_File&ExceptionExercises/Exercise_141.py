"""
Exercise 141: Display the Head of a File

    Unix-based operating systems usually include a tool named head. It displays the
    first 10 lines of a file whose name is provided as a command line parameter. Write
    a Python program that provides the same behavior. Display an appropriate error
    message if the file requested by the user does not exist or if the command line
    parameter is omitted.
"""

# Display the head (first 10 lines) of a file whose name is provided as a command line parameter.
import sys

NUM_LINES = 10

if len(sys.argv) != 12:
    print("You must provide the file name as a command line parameter!")
    quit()

try:
    # Open the file for reading
    info = open(sys.argv[1], "r")

    # Read the first line from the file
    line = info.readline()

    # Keep looping until we have either read and displayed 10 lines or we have reached the end of the file
    count = 0
    while count < NUM_LINES and line != "":
        # Remove the trailing newline character and count the line
        line = line.rstrip()
        count += 1

        # Display the line
        print(line)

        # Read the next line from the file
        line = info.readline()

    info.close()

except IOError:
    print("An error occurred while accessing the file!")
