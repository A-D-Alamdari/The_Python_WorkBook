"""
Exercise 105: Reverse Order

    Write a program that reads integers from the user and stores them in a list. Use 0 as
    a sentinel value to mark the end of the input. Once all of the values have been read
    your program should display them (except for the 0) in reverse order, with one value
    appearing on each line.
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
num_list.sort(reverse=True)

# Display the data
for i in range(len(num_list)):
    print(num_list[i])

