"""
Exercise 134: Unique Characters

    Create a program that determines and displays the number of unique characters in a
    string entered by the user. For example, Hello, World! has 10 unique characters
    while zzzhas only one unique character. Use a dictionary or set to solve this problem.
"""


def count_unique_characters(string):
    unique_characters = set(string)
    return len(unique_characters)


# Example usage
user_input = input("Enter a string: ")
result = count_unique_characters(user_input)
print("Number of unique characters:", result)
