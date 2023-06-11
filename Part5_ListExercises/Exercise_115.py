"""
Exercise 115: Pig Latin

    Pig Latin is a language constructed by transforming English words. While the origins
    of the language are unknown, it is mentioned in at least two documents from
    the nineteenth century, suggesting that it has existed for more than 100 years. The
    following rules are used to translate English into Pig Latin:
    • If theword begins with a consonant (including y), then all letters at the beginning of
    theword, up to the first vowel (excluding y), are removed and then added to the end
    of the word, followed by ay. For example, computer becomes omputercay
    and think becomes inkthay.
    • If the word begins with a vowel (not including y), then way is added to the end
    of the word. For example, algorithm becomes algorithmway and office
    becomes officeway.
    Write a program that reads a line of text from the user. Then your program should
    translate the line into Pig Latin and display the result. You may assume that the string
    entered by the user only contains lowercase letters and spaces.
"""


# Function that translate English words to Pig Latin language
# @param word: The word to be translated
# @return translated_word: The word in Pig Latin language
def translate_to_pig_latin(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = 'bcdfghjklmnpqrstvwxyz'

    # Make the entered word lowercase
    word = word.lower()
    # Check if the word begins with a vowel
    if word[0] in vowels:
        return word + 'way'

    # Find the index of the first vowel (excluding 'y')
    index = 0
    for i, letter in enumerate(word):
        if letter in vowels[1:] or letter == 'y':
            index = i
            break

    # Construct the translated word
    translated_word = word[index:] + word[:index] + 'ay'
    return translated_word


# Read a line of text from the user
line = input("Enter a line of text: ")

# Split the line into words
words = line.split()

# Translate each word to Pig Latin
translated_words = [translate_to_pig_latin(word) for word in words]

# Join the translated words back into a line
translated_line = ' '.join(translated_words)

# Display the translated line
print("Translated line: ", translated_line)
