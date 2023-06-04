"""
Exercise 54:Wavelengths of Visible Light

    The wavelength of visible light ranges from 380 to 750 nanometers (nm). While the
    spectrum is continuous, it is often divided into 6 colors as shown below:

                    Color       Wavelength (nm)
                    --------------------------------
                    Violet      380 to less than 450
                    Blue        450 to less than 495
                    Green       495 to less than 570
                    Yellow      570 to less than 590
                    Orange      590 to less than 620
                    Red         620 to 750

    Write a program that reads awavelength from the user and reports its color. Display
    an appropriate error message if the wavelength entered by the user is outside of the
    visible spectrum.
"""

# User input
wavelength = float(input("Enter the wavelength (in nm): "))

# Determine the color based on wavelength
if 380 <= wavelength < 450:
    color = "Violet"
elif 450 <= wavelength < 495:
    color = "Blue"
elif 495 <= wavelength < 570:
    color = "Green"
elif 570 <= wavelength < 590:
    color = "Yellow"
elif 590 <= wavelength < 620:
    color = "Orange"
elif 620 <= wavelength <= 750:
    color = "Red"
else:
    print("Error: The entered wavelength is outside the visible spectrum.")
    exit()

# Display the result
print(f"The wavelength {wavelength} nm corresponds to the color {color}.")

