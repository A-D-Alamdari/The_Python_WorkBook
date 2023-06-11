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
# Method 1:
print("First Method:")
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

# -------------------------------------------------------------------------------
# Method 2:
print("\nSecond Method:")
# Create three different lists to store negative, zero, and positive values
negatives = []
zeros = []
positives = []

# Get data from the user
line = input("Enter an integer (blank to quit): ")

while line != "":
    num = int(line)

    if num < 0:
        negatives.append(num)
    elif num > 0:
        positives.append(num)
    else:
        zeros.append(num)

    # Read the next line of input from the user
    line = input("Enter an integer (blank to quit): ")

# displays the numbers
print("The numbers that you entered are: ")
for i in negatives:
    print(i)

for i in zeros:
    print(i)

for i in positives:
    print(i)
