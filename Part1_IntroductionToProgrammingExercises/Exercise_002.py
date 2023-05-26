"""
Exercise 2: Hello

    Write a program that asks the user to enter his or her name. The program should
    respond with a message that says hello to the user, using his or her name.

"""

# Get the input from the user and assign it to a variable
user_name = input("Please Enter Your Name: ")

# Use concatenation to print hello + user name

# Method 1:
print("Hello,", user_name, "!")

# Method 2:
print(f"Hello, {user_name}!")

# Method 3:
print("Hello, {}!".format(user_name))

# Method 4:
print("Hello, " + user_name + "!")
