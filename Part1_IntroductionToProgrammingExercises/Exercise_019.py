"""
Exercise 19: Free Fall

    Create a program that determines how quickly an object is traveling when it hits the
    ground. The user will enter the height from which the object is dropped in meters (m).
    Because the object is dropped its initial speed is 0m/s. Assume that the acceleration
    due to gravity is 9.8m/s2. You can use the formula vf = sqrt(v_i ^ 2 + 2ad to compute the
    final speed, v_f , when the initial speed, v_i , acceleration, a, and distance, d, are known.
"""
# We need to import math library
import math

# Define the constants
GRAVITY = 9.8

# Get the user input
drop_height = float(input("Enter the height from which from the object is dropped in meters: "))

# Compute the velocity
v_f = math.sqrt(2 * GRAVITY * drop_height)

# Display the result
print("It will hit the ground at %.2f [m/s]." % v_f)
