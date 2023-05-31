"""
Exercise 85: Convert an Integer to its Ordinal Number

    Words like first, second and third are referred to as ordinal numbers. In this exercise,
    you will write a function that takes an integer as its only parameter and returns a
    string containing the appropriate English ordinal number as its only result. Your
    function must handle the integers between 1 and 12 (inclusive). It should return an
    empty string if a value outside of this range is provided as a parameter. Include a
    main program that demonstrates your function by displaying each integer from 1 to
    12 and its ordinal number. Your main program should only run when your file has
    not been imported into another program.
"""


def convert_to_ordinal(number):
    if number < 1 or number > 12:
        return ""

    ordinal_suffixes = {1: "st", 2: "nd", 3: "rd"}
    if 10 < number < 20:
        suffix = "th"
    else:
        suffix = ordinal_suffixes.get(number % 10, "th")

    return str(number) + suffix


def main():
    for number in range(1, 13):
        ordinal_number = convert_to_ordinal(number)
        print(f"{number} -> {ordinal_number}")


if __name__ == "__main__":
    main()
