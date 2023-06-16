"""
Exercise 155:Gender Neutral Names

    Some names, like Ben and Jonathan, are normally only used for boys while names
    like Rebbecca and Flora are normally only used for girls. Other names, like Chris
    and Alex, may be used for both boys and girls.
    Write a program that determines and displays all of the baby names that were
    used for both boys and girls in a year specified by the user. Your program should
    generate an appropriate message if there were no gender neutral names in the selected
    year. Display an appropriate error message if you do not have data for the year
    requested by the user. Additional details about the baby names data set are included
    in Exercise 154.
"""
import os


def get_gender_neutral_names(directory, year):
    gender_neutral_names = set()

    filename = f"{year}_BoysNames.txt"
    boy_file_path = os.path.join(directory, filename)
    filename = f"{year}_GirlsNames.txt"
    girl_file_path = os.path.join(directory, filename)

    if not os.path.isfile(boy_file_path) or not os.path.isfile(girl_file_path):
        print(f"No data available for the year {year}.")
        return gender_neutral_names

    with open(boy_file_path, "r") as boy_file, open(girl_file_path, "r") as girl_file:
        boy_names = {line.split()[0] for line in boy_file}
        girl_names = {line.split()[0] for line in girl_file}

    gender_neutral_names = boy_names.intersection(girl_names)

    return gender_neutral_names

# Directory containing the baby names data set
directory = "baby_names_data"  # Replace with the actual directory path

# Prompt the user to enter a year
year = input("Enter a year to find gender-neutral names: ")

# Get the gender-neutral names for the specified year
neutral_names = get_gender_neutral_names(directory, year)

if neutral_names:
    print(f"Gender-neutral names in {year}:")
    for name in neutral_names:
        print(name)
else:
    print(f"No gender-neutral names found in {year}.")
