"""
Exercise 84: Median of Three Values

    Write a function that takes three numbers as parameters, and returns the median value
    of those parameters as its result. Include a main program that reads three values from
    the user and displays their median.
    Hint: The median value is the middle of the three values when they are sorted
    into ascending order. It can be found using if statements, or with a little bit of
    mathematical creativity.
"""


# I write two different function to calculate the median

# First method to calculate the median of 3 numbers
# In this method, I used min() and max() built-in methods
def median_1(a, b, c):
    max_num = max(a, b, c)
    min_num = min(a, b, c)
    media_num = (a + b + c) - (min_num + max_num)
    return media_num


# Second method to calculate the median of 3 numbers
# In this method, I used if else statement
def median_2(a, b, c):
    if a <= b <= c or c <= b <= a:
        return b
    if b <= a <= c or c <= a <= b:
        return a
    if a <= c <= b or b <= c <= a:
        return c


# Define the main method
def main():
    x = float(input("Enter the first value: "))
    y = float(input("Enter the second value: "))
    z = float(input("Enter the third value: "))

    print(f"The median value is (Method 1): {median_1(x, y, z)}")
    print(f"The median value is (Method 2): {median_2(x, y, z)}")


# Call the main method
main()
