"""
Exercise 130:Text Messaging

    On some basic cell phones, text messages can be sent using the numeric keypad.
    Because each key has multiple letters associated with it, multiple key presses are
    needed for most letters. Pressing the number once generates the first letter on the
    key. Pressing the number 2, 3, 4 or 5 times generates the second, third, fourth or fifth
    character listed for that key.

                Key             Symbols
                -------------------------
                1               . , ? ! :
                2               A B C
                3               D E F
                4               G H I
                5               J K L
                6               M N O
                7               P Q R S
                8               T U V
                9               W X Y Z
                0               space

    Write a program that displays the key presses that must be made to enter a text
    message read from the user. Construct a dictionary that maps from each letter or
    symbol to the key presses. Then use the dictionary to generate and display the presses
    for the user’s message. For example, if the user enters Hello, World! then your
    program should output 4433555555666110966677755531111. Ensure that
    your program handles both uppercase and lowercase letters. Ignore any characters
    that aren’t listed in the table above such as semicolons and brackets.
"""


def get_key_presses(message):
    key_presses = ""

    char_to_key = {
        '.': '1', ',': '11', '?': '111', '!': '1111', ':': '11111',
        'a': '2', 'b': '22', 'c': '222',
        'd': '3', 'e': '33', 'f': '333',
        'g': '4', 'h': '44', 'i': '444',
        'j': '5', 'k': '55', 'l': '555',
        'm': '6', 'n': '66', 'o': '666',
        'p': '7', 'q': '77', 'r': '777', 's': '7777',
        't': '8', 'u': '88', 'v': '888',
        'w': '9', 'x': '99', 'y': '999', 'z': '9999',
        ' ': '0'
    }

    for char in message.lower():
        if char in char_to_key:
            key_presses += char_to_key[char]

    return key_presses


# Read the message from the user
message = input("Enter the message: ")

# Get the key presses for the message
key_presses = get_key_presses(message)

# Display the key presses
print(key_presses)
