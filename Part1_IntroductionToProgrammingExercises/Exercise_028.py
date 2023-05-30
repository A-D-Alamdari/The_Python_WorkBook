"""
Exercise 28:Wind Chill

    When the wind blows in cold weather, the air feels even colder than it actually is
    because the movement of the air increases the rate of cooling for warm objects, like
    people. This effect is known as wind chill.
    In 2001, Canada, the United Kingdom and the United States adopted the following
    formula for computing the wind chill index. Within the formula Ta is the
    air temperature in degrees Celsius and V is the wind speed in kilometers per hour.
    A similar formula with different constant values can be used with temperatures in
    degrees Fahrenheit and wind speeds in miles per hour.

            WCI = 13.12 + 0.6215*T_a − 11.37*V0.16 + 0.3965*T_a*Vˆ0.16

    Write a program that begins by reading the air temperature and wind speed from the
    user. Once these values have been read your program should display the wind chill
    index rounded to the closest integer.

    The wind chill index is only considered valid for temperatures less than or
    equal to 10 degrees Celsius and wind speeds exceeding 4.8 kilometers per
    hour.
"""

# Define constants
WC_OFFSET = 13.12
WC_FACTOR1 = 0.6215
WC_FACTOR2 = -11.37
WC_FACTOR3 = 0.3965
WC_EXPONENT = 0.16

# Get the user inputs
temp = float(input("Enter the air temperature (degrees Celsius): "))
speed = float(input("Enter the wind speed (km/h): "))

# Compute the wind chill index
wci = WC_OFFSET + \
      WC_FACTOR1 * temp + \
      WC_FACTOR2 * (speed ** WC_EXPONENT) + \
      WC_FACTOR3 * temp * (speed ** WC_EXPONENT)

# Display the result
print("The wind chill index is", round(wci))
