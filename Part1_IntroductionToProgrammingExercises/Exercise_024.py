"""
Exercise 24: Units of Time

    Create a program that reads a duration from the user as a number of days, hours,
    minutes, and seconds. Compute and display the total number of seconds represented
    by this duration.
"""

# Get the user inputs
days = int(input("Enter the number of days: "))
hours = int(input("Enter the number of hours: "))
minutes = int(input("Enter the number of minutes: "))
seconds = int(input("Enter the number of seconds: "))

# Calculate the total number of seconds
total_sec = seconds + minutes * 60 + hours * 60 * 60 + days * 24 * 60 * 60

# Display the result
print(f"The total number of seconds in {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds"
      f" is {total_sec}.")
