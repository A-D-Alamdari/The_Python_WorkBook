"""
Exercise 72: Is a String a Palindrome?

    A string is a palindrome if it is identical forward and backward. For example “anna”,
    “civic”, “level” and “hannah” are all examples of palindromic-words. Write a program
    that reads a string from the user and uses a loop to determines whether it is a
    palindrome. Display the result, including a meaningful output message.
"""

# Get input from the user
word_input = input("Enter a string: ")
word = word_input.lower()

is_palindrome = True

# Check the characters, string from the ends until
# the middle is reached
for i in range(len(word) // 2):
    # If the characters don't match then mark that the string is not a palindrome
    if word[i] != word[len(word) - i - 1]:
        is_palindrome = False

# Display the result
if is_palindrome:
    print(f"{word_input} is a palindrome.")
else:
    print(f"{word_input} is NOT a palindrome!")
