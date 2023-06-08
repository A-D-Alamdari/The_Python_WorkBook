"""
Exercise 102: Reduce Measures

    Many recipe books still use cups, tablespoons and teaspoons to describe the volumes
    of ingredients used when cooking or baking. While such recipes are easy enough to
    follow if you have the appropriate measuring cups and spoons, they can be difficult
    to double, triple or quadruple when cooking Christmas dinner for the entire extended
    family. For example, a recipe that calls for 4 tablespoons of an ingredient requires 16
    tablespoons when quadrupled. However, 16 tablespoons would be better expressed
    (and easier to measure) as 1 cup.
    Write a function that expresses an imperial volume using the largest units pos-
    sible. The function will take the number of units as its first parameter, and the unit
    of measure (cup, tablespoon or teaspoon) as its second parameter. Return a string
    representing the measure using the largest possible units as the function’s only result.
    For example, if the function is provided with parameters representing 59 teaspoons
    then it should return the string “1 cup, 3 tablespoons, 2 teaspoons”.

    Hint: One cup is equivalent to 16 tablespoons. One tablespoon is equivalent to
    3 teaspoons.
"""


def express_volume(units, unit_type):
    if unit_type == "cup":
        cups = units // 16
        tablespoons = (units % 16) // 3
        teaspoons = (units % 16) % 3
    elif unit_type == "tablespoon":
        cups = units // 16
        tablespoons = units % 16
        teaspoons = 0
    elif unit_type == "teaspoon":
        cups = units // 48
        tablespoons = (units % 48) // 3
        teaspoons = (units % 48) % 3

    result = ""
    if cups > 0:
        result += str(cups) + " cup" + ("s" if cups > 1 else "")
    if tablespoons > 0:
        if result:
            result += ", "
        result += str(tablespoons) + " tablespoon" + ("s" if tablespoons > 1 else "")
    if teaspoons > 0:
        if result:
            result += ", "
        result += str(teaspoons) + " teaspoon" + ("s" if teaspoons > 1 else "")

    return result


def main():
    units = int(input("Enter the number of units: "))
    unit_type = input("Enter the unit of measure (cup, tablespoon, teaspoon): ")

    result = express_volume(units, unit_type)
    print("Expressed volume:", result)


if __name__ == "__main__":
    main()
