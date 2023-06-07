"""
Exercise 86:The Twelve Days of Christmas

    The Twelve Days of Christmas is a repetitive song that describes an increasingly
    long list of gifts sent to one’s true love on each of 12 days. A single gift is sent on
    the first day. A new gift is added to the collection on each additional day, and then
    the complete collection is sent. The first three verses of the song are shown below.
    The complete lyrics are available on the internet.

        On the first day of Christmas
        my true love sent to me:
        A partridge in a pear tree.
        On the second day of Christmas
        my true love sent to me:
        Two turtle doves,
        And a partridge in a pear tree.
        On the third day of Christmas
        my true love sent to me:
        Three French hens,
        Two turtle doves,
        And a partridge in a pear tree.

    Your task is to write a program that displays the complete lyrics for The Twelve
    Days of Christmas. Write a function that takes the verse number as its only parameter
    and displays the specified verse of the song. Then call that function 12 times with
    integers that increase from 1 to 12.
    Each item that is sent to the recipient in the song should only appear once in your
    program, with the possible exception of the partridge. It may appear twice if that
    helps you handle the difference between “A partridge in a pear tree” in the first verse
    and “And a partridge in a pear tree” in the subsequent verses. Import your solution
    to Exercise 85 to help you complete this exercise.
"""


def display_verse(verse_number):
    gifts = [
        "A partridge in a pear tree.",
        "Two turtle doves,",
        "Three French hens,",
        "Four calling birds,",
        "Five golden rings,",
        "Six geese a-laying,",
        "Seven swans a-swimming,",
        "Eight maids a-milking,",
        "Nine ladies dancing,",
        "Ten lords a-leaping,",
        "Eleven pipers piping,",
        "Twelve drummers drumming,"
    ]

    ordinal_numbers = [
        "first", "second", "third", "fourth", "fifth", "sixth",
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
    ]

    print("On the", ordinal_numbers[verse_number - 1], "day of Christmas")
    print("my true love sent to me:")

    for i in range(verse_number - 1, -1, -1):
        if verse_number == 1 and i == 0:
            print(gifts[i])
        elif i == 0:
            print("And", gifts[i])
        else:
            print(gifts[i])


def main():
    for i in range(1, 13):
        display_verse(i)
        print()


if __name__ == '__main__':
    main()
