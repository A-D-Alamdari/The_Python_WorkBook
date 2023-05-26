"""
Exercise 1: Mailing Address

    Create a program that displays your name and complete mailing address formatted in
    the manner that you would usually see it on the outside of an envelope. Your program
    does not need to read any input from the user.
"""
my_name = "John Wick"
my_department = "Department of Computer Science"
my_university = "Ozyegin University"
my_address_line1 = "Nisantepe, Orman St., Ozyegin University, AB4 Building, B4 floor, Office No: B426"
my_address_line2 = "Cekmekoy-Istanbul"

# Method 1:
print("--------- Method 1 ---------")
print(my_name)
print(my_department)
print(my_university)
print(my_address_line1)
print(my_address_line2)

# Method 2
print("\n--------- Method 2 ---------")
print(f"{my_name}\n{my_department}\n{my_university}\n{my_address_line1}\n{my_address_line2}")
