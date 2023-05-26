"""
Exercise 4:Area of a Field

    Create a program that reads the length and width of a farmer’s field from the user in
    feet. Display the area of the field in acres.
        Hint: There are 43,560 square feet in an acre.
"""
# Since there are 43560 square feet in an acre, and it is constant number
# We can define a variable for this, which its name should be in uppercase.
SQFT_PER_ACRE = 43560

# Get information from user
length = float(input("Enter the length of the field in feet: "))
width = float(input("Enter the width of the field in feet: "))

# Compute the area of the field in square feet
area_in_sqft = length * width

# Convert the area in square feet to acre
area_in_acre = area_in_sqft / SQFT_PER_ACRE

# Print the result
print(f"The area of the field is {area_in_sqft} square feet or {area_in_acre} acres.")

