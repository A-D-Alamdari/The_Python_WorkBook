"""
Exercise 167: Recursive Palindrome

    The notion of a palindrome was introduced previously in Exercise 72. In this exer-
    cise you will write a recursive function that determines whether or not a string is
    a palindrome. The empty string is a palindrome, as is any string containing only
    one character. Any longer string is a palindrome if its first and last characters
    match, and if the string formed by removing the first and last characters is also
    a palindrome.
    Write a main program that reads a string from the user. Use your recursive function
    to determine whether or not the string is a palindrome. Then display an appropriate
    message for the user.
"""


def is_palindrome(string):
    if len(string) <= 1:
        return True
    elif string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    else:
        return False


user_input = input("Enter a string: ")

if is_palindrome(user_input.lower()):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

