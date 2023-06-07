"""
Exercise 87: Center a String in the Terminal

    Write a function that takes a string of characters as its first parameter, and the width of
    the terminal in characters as its second parameter. Your function should return a new
    string that consists of the original string and the correct number of leading spaces
    so that the original string will appear centered within the provided width when it is
    printed. Do not add any characters to the end of the string. Include a main program
    that demonstrates your function.
"""


def center_string(string, width):
    if len(string) >= width:
        return string  # No need to center if the string is wider than the width

    num_spaces = (width - len(string)) // 2
    centered_string = ' ' * num_spaces + string

    return centered_string


def main():
    string = "Hello, World!"
    width = 20

    centered_string = center_string(string, width)
    print(centered_string)


if __name__ == '__main__':
    main()
