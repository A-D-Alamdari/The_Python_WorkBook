"""
Exercise 169: String Edit Distance

    The edit distance between two strings is a measure of their similarity—the smaller the
    edit distance, the more similar the strings are with regard to the minimum number of
    insert, delete and substitute operations needed to transform one string into the other.
    Consider the strings kitten and sitting. The first string can be transformed
    into the second string with the following operations: Substitute the k with an s,
    substitute the e with an i, and insert a g at the end of the string. This is the smallest
    number of operations that can be performed to transform kitten into sitting.
    As a result, the edit distance is 3.
    Write a recursive function that computes the edit distance between two strings.
    Use the following algorithm:

        Let s and t be the strings
        If the length of s is 0 then
            Return the length of t
        Else if the length of t is 0 then
            Return the length of s
        Else
            Set cost to 0
            If the last character in s does not equal the last character in t
                then
                    Set cost to 1
            Set d1 equal to the edit distance between all characters except the last one
            in s, and all characters in t , plus 1
            Set d2 equal to the edit distance between all characters in s, and all
            characters except the last one in t , plus 1
            Set d3 equal to the edit distance between all characters except the last one
            in s, and all characters except the last one in t , plus cost
            Return the minimum of d1, d2 and d3

    Use your recursive function to write a program that reads two strings from the
    user and displays the edit distance between them.
"""


# Compute the edit distance between two strings as a count for the minimum number of insert,
# delete, and substitute operations needed to transform one string into the other.
def edit_distance(string1, string2):
    # If one string is empty, then the edit distance is one insert operation for each letter in the other string.
    if len(string1) == 0:
        return len(string2)
    elif len(string2) == 0:
        return len(string1)
    else:
        cost = 0
        # If the last characters are not equal, set cost to 1
        if string1[len(string1) - 1] != string2[len(string2) - 1]:
            cost = 1
        # Compute three distances
        d1 = edit_distance(string1[0: len(string1) - 1], string2) + 1
        d2 = edit_distance(string1, string2[0: len(string2) - 1]) + 1
        d3 = edit_distance(string1[0: len(string1) - 1], string2[0: len(string2) - 1]) + cost
        return min(d1, d2, d3)


# Compute the edit distance between two strings entered by the user
def main():
    # Read input from the user
    string1 = input("Enter a string: ")
    string2 = input("Enter another string: ")

    # Compute and display the result
    print("The edit distance between %s and %s is %d." % (string1, string2, edit_distance(string1, string2)))


main()
