"""
Exercise 108: Negatives,Zeros and Positives

    Create a program that reads integers from the user until a blank line is entered. Once
    all of the integers have been read your program should display all of the negative
    numbers, followed by all of the zeros, followed by all of the positive numbers.Within
    each group the numbers should be displayed in the same order that they were entered
    by the user. For example, if the user enters the values 3, -4, 1, 0, -1, 0, and -2 then
    your program should output the values -4, -1, -2, 0, 0, 3, and 1. Your program
    should display each value on its own line.
"""

# Create a list
nums = list()
user = None

# Get the user input
while True:
    user = input("Enter an integer (for quit press enter): ")
    if user == "":
        print("You terminated the program!")
        break
    else:
        user = int(user)
        nums.append(user)

# Display the result
print("\nYour entered values are:")
for i in sorted(nums):
    print(i)
