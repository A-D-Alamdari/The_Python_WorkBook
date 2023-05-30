"""
Exercise 29: Celsius to Fahrenheit and Kelvin

    Write a program that begins by reading a temperature from the user in degrees
    Celsius. Then your program should display the equivalent temperature in degrees
    Fahrenheit and degrees Kelvin. The calculations needed to convert between different
    units of temperature can be found on the internet.
"""

# Get the user input
temp_cel = float(input("Enter the temperature in degrees Celsius: "))

# Convert the temperature
temp_k = (temp_cel * 9 / 5) + 32
temp_f = temp_cel + 273.15

# display the result
print("The %.2f degrees Celsius is equivalent to %.2f degrees Kelvin and %.2f "
      "degrees Fahrenheit." % (temp_cel, temp_k, temp_f))
