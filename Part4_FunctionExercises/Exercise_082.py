"""
Exercise 82:Taxi Fare

    In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25
    for every 140 meters traveled. Write a function that takes the distance traveled (in
    kilometers) as its only parameter and returns the total fare as its only result. Write a
    main program that demonstrates the function.

    Hint: Taxi fares change over time. Use constants to represent the base fare and
    the variable portion of the fare so that the program can be updated easily when
    the rates increase.
"""

BASE_FARE = 4.0
FARE_PER_METERS = 0.25


# Define the function

# Function to calculate the Taxi Fare
# @param distance: Distance travelled in meters
# @return The total taxi fare
def taxi_fare(distance):
    number_of_sub_distance = distance // 140
    total_fare = BASE_FARE + number_of_sub_distance * FARE_PER_METERS
    return total_fare


# Get input from the user
distance = int(input("Enter the total distance in meters: "))

# Calculate the far
total_fare = taxi_fare(distance)

# Display the result to the user
print("The taxi fare for your trip is: $%0.2f." % total_fare)
