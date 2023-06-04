"""
Exercise 56: Cell Phone Bill

    A particular cell phone plan includes 50 minutes of air time and 50 text messages
    for $15.00 a month. Each additional minute of air time costs $0.25, while additional
    text messages cost $0.15 each. All cell phone bills include an additional charge of
    $0.44 to support 911 call centers, and the entire bill (including the 911 charge) is
    subject to 5 percent sales tax.
    Write a program that reads the number of minutes and text messages used in a
    month from the user. Display the base charge, additional minutes charge (if any),
    additional text message charge (if any), the 911 fee, tax and total bill amount. Only
    display the additional minute and text message charges if the user incurred costs in
    these categories. Ensure that all of the charges are displayed using 2 decimal places.
"""

# Constants
BASE_CHARGE = 15.00
ADDITIONAL_MINUTE_CHARGE = 0.25
ADDITIONAL_MESSAGE_CHARGE = 0.15
FEE_911 = 0.44
SALES_TAX_RATE = 0.05

# User inputs
minutes_used = int(input("Enter the number of minutes used: "))
messages_used = int(input("Enter the number of text messages used: "))

# Calculate additional charges
additional_minute_charge = max(minutes_used - 50, 0) * ADDITIONAL_MINUTE_CHARGE
additional_message_charge = max(messages_used - 50, 0) * ADDITIONAL_MESSAGE_CHARGE

# Calculate total charges
subtotal = BASE_CHARGE + additional_minute_charge + additional_message_charge + FEE_911
tax = subtotal * SALES_TAX_RATE
total_bill = subtotal + tax

# Display the bill details
print(f"Base Charge: ${BASE_CHARGE:.2f}")
if additional_minute_charge > 0:
    print(f"Additional Minutes Charge: ${additional_minute_charge:.2f}")
if additional_message_charge > 0:
    print(f"Additional Messages Charge: ${additional_message_charge:.2f}")
print(f"911 Fee: ${FEE_911:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total Bill: ${total_bill:.2f}")

