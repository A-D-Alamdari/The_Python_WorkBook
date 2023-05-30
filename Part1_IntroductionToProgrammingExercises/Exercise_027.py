"""
Exercise 27: Body Mass Index

    Write a program that computes the body mass index (BMI) of an individual. Your
    program should begin by reading a height and weight from the user. Then it should
    use one of the following two formulas to compute the BMI before displaying it. If
    you read the height in inches and the weight in pounds then body mass index is
    computed using the following formula:
                    BMI = weight / (height × height) × 703.
    If you read the height in meters and the weight in kilograms then body mass index
    is computed using this slightly simpler formula:
                    BMI = weight / (height × height)
"""

# Since we don't allow to use if-else statements in this section, I continue to write this Exercise
# only for metric system.

# Get the inputs from the user
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate the BMI
BMI_1 = weight / (height * height)

# Display the result
print("Your BMI is %.2f." % BMI_1)

# The Following Part is for Height in Inches and Weight in Pounds
# Get the inputs from the user
weight_lb = float(input("Enter your weight in pounds: "))
height_in = float(input("Enter your height in inches: "))

# Calculate the BMI
BMI_2 = weight_lb / (height_in * height_in) * 703

# Display the result
print("Your BMI is %.2f." % BMI_2)
