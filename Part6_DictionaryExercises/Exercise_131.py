"""
Exercise 131: Morse Code

    Morse code is an encoding scheme that uses dashes and dots to represent numbers
    and letters. In this exercise, you will write a program that uses a dictionary to store
    the mapping from letters and numbers to Morse code. Use a period to represent a dot,
    and a hyphen to represent a dash. The mapping from letters and numbers to dashes
    and dots is shown in Table 6.1.
    Your program should read a message from the user. Then it should translate each
    letter and number in the message to Morse code, leaving a space between each
    sequence of dashes and dots. Your program should ignore any characters that are not
    letters or numbers. The Morse code for Hello, World! is shown below:

                    .... . .-.. .-.. --- .-- --- .-. .-.. -..

    Table 6.1 - Morse Code Letters and Numbers

    Letter      Code        Letter      Code        Letter      Code        Number      Code
    ----------------------------------------------------------------------------------------
    A           .-          J           .- - -      S           ...         1           .- - - -
    B           -...        K           -.-         T           -           2           ..---
    C           -.-.        L           .-..        U           ..-         3           ...- -
    D           -..         M           - -         V           ...-        4           ....-
    E           .           N           -.          W           .- -        5           .....
    F           ..-.        O           - - -       X           -..-        6           -....
    G           - -.        P           .- -.       Y           -.- -       7           - -...
    H           ....        Q           - -.-       Z           - -..       8           - - -..
    I           ..          R           .-.         0           - - - - -   9           ----.

    Morse code was originally developed in the nineteenth century for use over
    telegraph wires. It is still used today, over 160 years after it was first created.
"""


def morse_code_translator(message):
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '-.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.'
    }

    translated_message = []
    for char in message:
        if char.isalnum():
            char = char.upper()
            if char in morse_code:
                translated_message.append(morse_code[char])

    return ' '.join(translated_message)


# Example usage
user_input = input("Enter a message: ")
result = morse_code_translator(user_input)
print(result)
