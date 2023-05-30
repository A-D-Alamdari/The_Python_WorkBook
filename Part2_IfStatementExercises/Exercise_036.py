"""
Exercise 36:Vowel or Consonant

    In this exercise you will create a program that reads a letter of the alphabet from the
    user. If the user enters a, e, i, o or u then your program should display a message
    indicating that the entered letter is a vowel. If the user enters y then your program
    should display a message indicating that sometimes y is a vowel, and sometimes y is
    a consonant. Otherwise your program should display a message indicating that the
    letter is a consonant.
"""

# Get the letter from the user
letter = input("Enter a letter of the alphabet: ")
letter = letter.lower()
# Classify the letter as vowel or consonant
if letter in ["a", "e", "i", "o", "u"]:
    print("It is a Vowel letter.")
elif letter == "y":
    print("Sometimes it is a Vowel, and somtimes it is a Consonant.")
else:
    print("It is a Consonant letter.")
