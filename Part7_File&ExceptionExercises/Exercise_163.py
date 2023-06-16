"""
Exercise 163:Words with Six Vowels in Order

    There is at least one word in the English language that contains each of the vowels
    a, e, i , o, u and y exactly once and in order. Write a program that searches a file
    containing a list of words and displays all of the words that meet this constraint. The
    user will provide the name of the file that will be searched. Display an appropriate
    error message and exit the program if the user provides an invalid file name or if
    something else goes wrong while searching for words with six vowels in order.
"""


def find_words_with_six_vowels(file_name):
    try:
        with open(file_name, 'r') as file:
            for word in file:
                word = word.strip().lower()
                vowels = ['a', 'e', 'i', 'o', 'u', 'y']
                if all(vowels[i] in word for i in range(6)):
                    print(word)
    except FileNotFoundError:
        print("Invalid file name. Please provide a valid file name.")
    except:
        print("Something went wrong while searching for words.")


# Prompt the user for the file name
file_name = input("Enter the name of the file to search: ")
find_words_with_six_vowels(file_name)
