"""
Exercise 89: Capitalize It

    Many people do not use capital letters correctly, especially when typing on small
    devices like smart phones. In this exercise, you will write a function that capitalizes
    the appropriate characters in a string. A lowercase “i” should be replaced with an
    uppercase “I” if it is both preceded and followed by a space. The first character in
    the string should also be capitalized, as well as the first non-space character after a
    “.”, “!” or “?”. For example, if the function is provided with the string “what time
    do i have to be there? what’s the address?” then it should return the string “What
    time do I have to be there? What’s the address?”. Include a main program that reads
    a string from the user, capitalizes it using your function, and displays the result.
"""


def capitalize_string(string):
    result = ''
    capitalize_next = True

    for i in range(len(string)):
        if capitalize_next and string[i].isalpha():
            result += string[i].upper()
            capitalize_next = False
        else:
            result += string[i]

        if string[i] in ['.', '!', '?']:
            capitalize_next = True
        elif string[i] == 'i' and (i == 0 or string[i - 1] == ' ') and (i == len(string) - 1 or string[i + 1] == ' '):
            result = result[:-1] + 'I'

    return result


def main():
    string = input("Enter a string: ")
    capitalized_string = capitalize_string(string)
    print(capitalized_string)


if __name__ == '__main__':
    main()
