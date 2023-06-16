"""
Exercise 160: Redacting Text in a File

    Sensitive information is often removed, or redacted, from documents before they
    are released to the public. When the documents are released it is common for the
    redacted text to be replaced with black bars.
    In this exercise you will write a program that redacts all occurrences of sensitive
    words in a text file by replacing them with asterisks. Your program should redact
    sensitive words wherever they occur, even if they occur in the middle of another
    word. The list of sensitive words will be provided in a separate text file. Save the
    redacted version of the original text in a new file. The names of the original text file,
    sensitive words file, and redacted file will all be provided by the user.
    You may find the replace method for strings helpful when completing this
    exercise. Information about the replace method can either be found in your
    textbook or on the internet.
    For an added challenge, extend your program so that it redacts words in a case
    insensitive manner. For example, if exam appears in the list of sensitive words then
    redact exam, Exam, ExaM and EXAM, among other possible capitalizations.
"""


def redact_text(original_file, sensitive_words_file, redacted_file):
    # Read sensitive words from the file
    with open(sensitive_words_file, 'r') as file:
        sensitive_words = [word.strip().lower() for word in file.readlines()]

    # Read the original text file
    with open(original_file, 'r') as file:
        original_text = file.read()

    # Redact sensitive words in the original text
    redacted_text = original_text.lower()
    for word in sensitive_words:
        redacted_text = redacted_text.replace(word, '*' * len(word))

    # Write the redacted text to a new file
    with open(redacted_file, 'w') as file:
        file.write(redacted_text)


# Prompt the user for file names
original_file = input("Enter the name of the original text file: ")
sensitive_words_file = input("Enter the name of the file containing sensitive words: ")
redacted_file = input("Enter the name of the redacted file: ")

# Redact the text and save it to a new file
redact_text(original_file, sensitive_words_file, redacted_file)

print("Redacted file has been created successfully.")
