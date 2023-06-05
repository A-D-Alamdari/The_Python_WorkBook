"""
Exercise 70: Caesar Cipher

    One of the first known examples of encryption was used by Julius Caesar. Caesar
    needed to provide written instructions to his generals, but he didn’t want his enemies
    to learn his plans if the message slipped into their hands. As result, he developed
    what later became known as the Caesar Cipher.
    The idea behind this cipher is simple (and as a result, it provides no protection
    against modern code breaking techniques). Each letter in the original message is
    shifted by 3 places. As a result, A becomes D, B becomes E, C becomes F, D
    becomes G, etc. The last three letters in the alphabet are wrapped around to the
    beginning: X becomes A, Y becomes B and Z becomes C. Non-letter characters are
    not modified by the cipher.
    Write a program that implements a Caesar cipher. Allow the user to supply the
    message and the shift amount, and then display the shifted message. Ensure that
    your program encodes both uppercase and lowercase letters. Your program should
    also support negative shift values so that it can be used both to encode messages and
    decode messages.
"""

# Get user input
message = input("Enter the message: ")
shift = int(input("Enter the shift amount: "))

encrypted_message = ""
for char in message:
    if char.isalpha():
        # Determine the base offset based on the character type (uppercase or lowercase)
        if char.isupper():
            base_offset = ord('A')
        else:
            base_offset = ord('a')

        # Calculate the new position after shifting
        shifted_position = (ord(char) - base_offset + shift) % 26

        # Convert the shifted position back to a character and add it to the encrypted message
        encrypted_char = chr(base_offset + shifted_position)
        encrypted_message += encrypted_char
    else:
        # Non-letter characters are not modified by the cipher
        encrypted_message += char

# Display the encrypted message
print("Encrypted message:", encrypted_message)

