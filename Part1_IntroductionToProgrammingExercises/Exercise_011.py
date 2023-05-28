"""
Exercise 11: Fuel Efficiency

    In the United States, fuel efficiency for vehicles is normally expressed in miles-per-gallon
    (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
    kilometers (L/100 km). Use your research skills to determine how to convert from
    MPGto L/100 km. Then create a program that reads a value from the user in American
    units and displays the equivalent fuel efficiency in Canadian units.
"""
MPG_TO_LPK = 235.215

# Get user input
american_unit = float(input("Please enter your fuel efficiency in American units: "))

# compute in Canadian units
canadian_unit = MPG_TO_LPK / american_unit

# Display the results
print("The value of your fuel efficiency in Canadian unit is %.3f [L/100 km]." % canadian_unit)

