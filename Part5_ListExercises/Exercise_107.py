"""
Exercise 107:Avoiding Duplicates

    In this exercise, you will create a program that reads words from the user until the
    user enters a blank line. After the user enters a blank line your program should display
    each word entered by the user exactly once. The words should be displayed in
    the same order that they were entered. For example, if the user enters:
        first
        second
        first
        third
        second

    then your program should display:
        first
        second
        third
"""

# Create a list o add the inputs
input_list = list()

user_input = None

# Get the input from the user
while True:
    user_input = input("Enter a word (for quit press enter): ")
    if user_input == "":
        print("The program terminated!")
        break
    else:
        if user_input not in input_list:
            input_list.append(user_input)

# display the result
print("You entered:")
for item in input_list:
    print(item)
