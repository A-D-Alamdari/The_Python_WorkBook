"""
Exercise 61:Average

    In this exercise you will create a program that computes the average of a collection
    of values entered by the user. The user will enter 0 as a sentinel value to indicate
    that no further values will be provided. Your program should display an appropriate
    error message if the first value entered by the user is 0.
    Hint: Because the 0 marks the end of the input it should not be included in the
    average.
"""

count = 0
sums = 0.0
average = 0

# Since the number of iterations are not known we need to use while loop
while True:
    # Get user input
    user_input = float(input("Enter the number (enter 0 for exit): "))
    if count == 0 and user_input == 0.0:
        print("You terminate the program without entering a number!")
        break
    else:
        if user_input != 0.0:
            count += 1
            sums += user_input
        else:
            average = sums / count
            print("The average of entered numbers is: %.2f." % average)
            break

