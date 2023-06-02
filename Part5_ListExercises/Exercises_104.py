"""
Exercise 104: Sorted Order

    Write a program that reads integers from the user and stores them in a list. Your
    program should continue reading values until the user enters 0. Then it should display
    all of the values entered by the user (except for the 0) in order from smallest to largest,
    with one value appearing on each line. Use either the sort method or the sorted
    function to sort the list.
"""

# Declare a list
num_list = list()

user_input = 1

while user_input != 0:
    user_input = int(input("Enter your number (0 to quit): "))
    if user_input == 0:
        break
    else:
        num_list.append(user_input)

# Sort the list
num_list.sort()

# Display the data
for i in range(len(num_list)):
    print(num_list[i])
