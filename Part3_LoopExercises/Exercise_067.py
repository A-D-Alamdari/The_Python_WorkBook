"""
Exercise 67:Admission Price

    A particular zoo determines the price of admission based on the age of the guest.
    Guests 2 years of age and less are admitted without charge. Children between 3 and
    12 years of age cost $14.00. Seniors aged 65 years and over cost $18.00. Admission
    for all other guests is $23.00.
    Create a program that begins by reading the ages of all of the guests in a group
    from the user, with one age entered on each line. The user will enter a blank line to
    indicate that there are no more guests in the group. Then your program should display
    the admission cost for the group with an appropriate message. The cost should be
    displayed using two decimal places.
"""

# Ticket prices
CHILD_TICKET_PRICE = 14.00
ADULT_TICKET_PRICE = 23.00
SENIOR_TICKET_PRICE = 18.00

# Initialize variables
total_cost = 0

# Read ages of guests from the user
while True:
    age_input = input("Enter the age of a guest (or leave blank to finish): ")

    # Check if the user entered a blank line
    if age_input == "":
        break

    # Convert age input to integer
    age = int(age_input)

    # Calculate ticket price based on age
    if age <= 2:
        # Guests 2 years and younger are admitted without charge
        ticket_price = 0
    elif 3 <= age <= 12:
        # Children between 3 and 12 years old
        ticket_price = CHILD_TICKET_PRICE
    elif age >= 65:
        # Seniors aged 65 years and over
        ticket_price = SENIOR_TICKET_PRICE
    else:
        # All other guests
        ticket_price = ADULT_TICKET_PRICE

    # Add ticket price to the total cost
    total_cost += ticket_price

# Display the admission cost for the group
print("Admission cost for the group: $%.2f" % total_cost)
