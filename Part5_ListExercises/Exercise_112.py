"""
Exercise 112: Below and Above Average

    Write a program that reads numbers from the user until a blank line is entered. Your
    program should display the average of all of the values entered by the user. Then
    the program should display all of the below average values, followed by all of the
    average values (if any), followed by all of the above average values. An appropriate
    label should be displayed before each list of values.
"""

# Create an empty list to store the user inputs
nums = []

# Get input from user
line = input("Enter a number (blank to quit): ")

while line != "":
    num = float(line)
    nums.append(num)

    line = input("Enter a number (blank to quit): ")

# Calculate the average
sums = 0
for i in nums:
    sums += i

average = sums / len(nums)

# Create lists to store related data
below = []
same = []
above = []

for n in nums:
    if n < average:
        below.append(n)
    elif n == average:
        same.append(n)
    else:
        above.append(n)


# Display the result
print(f"\nThe average of entered numbers are: {average}")

print("\nThe numbers below the average:")
# Below values
for n in below:
    print(n, end="  ")

print("\nThe numbers same as the average:")
# Same values
if len(same) == 0:
    print(">> There is no value same as the average.")
else:
    for n in same:
        print(n, end="  ")
    print()

print("The numbers above the average:")
# Above values
for n in above:
    print(n, end="  ")
