"""
Exercise 30: Units of Pressure

    In this exercise you will create a program that reads a pressure from the user in kilopascals.
    Once the pressure has been read your program should report the equivalent
    pressure in pounds per square inch, millimeters of mercury and atmospheres. Use
    your research skills to determine the conversion factors between these units.
"""

# Conversion factors
KPA_TO_PSI = 0.145038
KPA_TO_MMHG = 7.50062
KPA_TO_ATM = 0.00986923

# Read pressure in kilopascals from the user
kpa = float(input("Enter pressure in kilopascals: "))

# Convert to pounds per square inch
psi = kpa * KPA_TO_PSI

# Convert to millimeters of mercury
mmhg = kpa * KPA_TO_MMHG

# Convert to atmospheres
atm = kpa * KPA_TO_ATM

# Display the converted pressures
print("Pressure in pounds per square inch (psi): %.3f" % psi)
print("Pressure in millimeters of mercury (mmHg): %.3f" % mmhg)
print("Pressure in atmospheres (atm): %.3f" % atm)

