"""
Exercise 73: MultipleWord Palindromes

    There are numerous phrases that are palindromes when spacing is ignored. Examples
    include “go dog”, “flee to me remote elf” and “some men interpret nine memos”,
    among many others. Extend your solution to Exercise 72 so that it ignores spacing
    while determining whether a string is a palindrome. For an additional challenge,
    extend your solution so that is also ignores punctuation marks and treats uppercase
    and lowercase letters as equivalent.
"""

# Read the phrase from the user
phrase = input("Enter a phrase: ")


# Remove spacing and punctuation marks
cleaned_phrase = ""
for char in phrase:
    if char.isalnum():
        cleaned_phrase += char.lower()

# Check if the cleaned phrase is a palindrome
is_palindrome = True
length = len(cleaned_phrase)
for i in range(length // 2):
    if cleaned_phrase[i] != cleaned_phrase[length - i - 1]:
        is_palindrome = False
        break

# Display the result
if is_palindrome:
    print("The phrase is a palindrome.")
else:
    print("The phrase is not a palindrome.")

