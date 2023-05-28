"""
Exercise 8:Widgets and Gizmos

    An online retailer sells two products: widgets and gizmos. Each widget weighs 75
    grams. Each gizmo weighs 112 grams. Write a program that reads the number of
    widgets and the number of gizmos in an order from the user. Then your program
    should compute and display the total weight of the order.
"""

# We have to constant value as follows
WEIGHT_WIDGET = 75
WEIGHT_GIZMO = 112

# Get the number of items from the user
num_widget = int(input("Enter the number of Widgets you are ordered: "))
num_gizmo = int(input("Enter the number of Gizmos you are ordered: "))

# compute the weights
widgets_weight = num_widget * WEIGHT_WIDGET
gizmos_weight = num_gizmo * WEIGHT_GIZMO
total_weight = widgets_weight + gizmos_weight

# display the result
print(f"The total weight of your order is {total_weight} grams.")
