"""
Exercise 143: ConcatenateMultiple Files

    Unix-based operating systems typically include a tool named cat, which is short
    for concatenate. Its purpose is to concatenate and display one or more files whose
    names are provided as command line parameters. The files are displayed in the same
    order that they appear on the command line.
    Create a Python program that performs this task. It should generate an appropriate
    error message for any file that cannot be displayed, and then proceed to the next file.
    Display an appropriate error message if your program is started without any command
    line parameters.
"""

import sys

if len(sys.argv) < 2:
    print("You must provide at least one file name as a command line parameter!")
    quit()

try:
    for i in range(1, len(sys.argv)):
        filename = sys.argv[i]
        with open(filename, "r") as file:
            content = file.read()
            print(content)

except FileNotFoundError as e:
    print(f"File not found: {e.filename}")
except IOError as e:
    print(f"An error occurred while accessing the file: {e.filename}")
