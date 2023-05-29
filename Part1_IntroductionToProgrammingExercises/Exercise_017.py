"""
Exercise 17: Heat Capacity

    The amount of energy required to increase the temperature of one gram of a material
    by one degree Celsius is the material’s specific heat capacity, C. The total amount
    of energy required to raise m grams of a material by delta(T) degrees Celsius can be
    computed using the formula:
                                q = mC delta(T).
    Write a program that reads the mass of some water and the temperature change
    from the user. Your program should display the total amount of energy that must be
    added or removed to achieve the desired temperature change.

    Hint: The specific heat capacity of water is 4.186 J/g◦C. Because water has a density
    of 1.0 gram per millilitre, you can use grams and millilitres interchangeably
    in this exercise.

    Extend your program so that it also computes the cost of heating the water. Electricity
    is normally billed using units of kilowatt hours rather than Joules. In this
    exercise, you should assume that electricity costs 8.9 cents per kilowatt-hour. Use
    your program to compute the cost of boiling water for a cup of coffee.

    Hint: You will need to look up the factor for converting between Joules and
    kilowatt hours to complete the last part of this exercise.
"""

# We need to define our constants values
WATER_HEAT_CAPACITY = 4.186
ELECTRICITY_PRICE = 8.9
J_TO_KWH = 2.777e-7     # Scientific notation of 2.777 * (10 ^-7)

# Get the data from the user
volume_water = float(input("Enter the amount of the water in milliliters: "))
delta_temp = float(input("Enter the temperature increase (◦C): "))

# compute the energy in Joules
q = volume_water * delta_temp * WATER_HEAT_CAPACITY

# Compute the cost
kwh = q * J_TO_KWH
cost = kwh * ELECTRICITY_PRICE

# Display the result
print("That will require %d Joules of energy." % q)
print("That much energy will cost %.2f cents." % cost)

