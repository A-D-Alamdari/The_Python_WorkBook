"""
Exercise 152:What’s that Element Again?

    Write a program that reads a file containing information about chemical elements
    and stores it in one or more appropriate data structures. Then your program should
    read and process input from the user. If the user enters an integer then your program
    should display the symbol and name of the element with the number of protons
    entered. If the user enters a string then your program should display the number
    of protons for the element with that name or symbol. Your program should display
    an appropriate error message if no element exists for the name, symbol or num-
    ber of protons entered. Continue to read input from the user until a blank line is
    entered.
"""


def create_element_dictionary(file_name):
    elements = {}

    with open(file_name, "r") as file:
        for line in file:
            line = line.strip().split(",")
            number = int(line[0])
            symbol = line[1]
            name = line[2]

            elements[number] = {"symbol": symbol, "name": name}
            elements[symbol] = {"number": number, "name": name}
            elements[name] = {"number": number, "symbol": symbol}

    return elements


def find_element(elements, query):
    query = query.strip().capitalize()

    if query.isdigit():
        query = int(query)
        if query in elements:
            return elements[query]
    else:
        if query in elements:
            return elements[query]

    return None


# Read the file and create the element dictionary
file_name = "elements.txt"  # Replace with the actual file path
element_dict = create_element_dictionary(file_name)

# Process user input
while True:
    user_input = input("Enter an element symbol, name, or number of protons (blank to quit): ")

    if user_input == "":
        break

    result = find_element(element_dict, user_input)
    if result:
        if "number" in result:
            print("Number of Protons:", result["number"])
        if "symbol" in result:
            print("Symbol:", result["symbol"])
        if "name" in result:
            print("Name:", result["name"])
    else:
        print("Element not found.")
