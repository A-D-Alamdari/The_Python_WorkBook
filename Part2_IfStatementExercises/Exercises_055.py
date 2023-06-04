"""
Exercise 55: Frequency to Name

    Electromagnetic radiation can be classified into one of 7 categories according to its
    frequency, as shown in the table below:

                Name                Frequency range (Hz)
                ------------------------------------------------------
                Radio waves         Less than 3 × 109
                Microwaves          3 × 10ˆ9 to less than 3 × 10ˆ12
                Infrared light      3 × 10ˆ12 to less than 4.3 × 10ˆ14
                Visible light       4.3 × 10ˆ14 to less than 7.5 × 10ˆ14
                Ultraviolet light   7.5 × 10ˆ14 to less than 3 × 10ˆ17
                X-rays              3 × 10ˆ17 to less than 3 × 10ˆ19
                Gamma rays          3 × 10ˆ19 or more

    Write a program that reads the frequency of the radiation from the user and displays
    the appropriate name.
"""

# User input
frequency = float(input("Enter the frequency (in Hz): "))

# Determine the radiation name based on frequency
if frequency < 3e9:
    radiation_name = "Radio waves"
elif frequency < 3e12:
    radiation_name = "Microwaves"
elif frequency < 4.3e14:
    radiation_name = "Infrared light"
elif frequency < 7.5e14:
    radiation_name = "Visible light"
elif frequency < 3e17:
    radiation_name = "Ultraviolet light"
elif frequency < 3e19:
    radiation_name = "X-rays"
else:
    radiation_name = "Gamma rays"

# Display the result
print(f"The radiation with a frequency of {frequency:.2e} Hz is classified as {radiation_name}.")

