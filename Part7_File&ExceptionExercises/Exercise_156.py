"""
Exercise 156: Most Births in a given Time Period

    Write a program that uses the baby names data set described in Exercise 154 to
    determine which names were used most often within a time period. Have the user
    supply the first and last years of the range to analyze. Display the boy’s name and
    the girl’s name given to the most children during the indicated years.
"""
import os


def get_most_common_names(directory, start_year, end_year):
    boy_names = {}
    girl_names = {}

    for year in range(start_year, end_year + 1):
        boy_filename = f"{year}_BoysNames.txt"
        boy_file_path = os.path.join(directory, boy_filename)

        girl_filename = f"{year}_GirlsNames.txt"
        girl_file_path = os.path.join(directory, girl_filename)

        if not os.path.isfile(boy_file_path) or not os.path.isfile(girl_file_path):
            print(f"No data available for the year {year}. Skipping...")
            continue

        with open(boy_file_path, "r") as boy_file, open(girl_file_path, "r") as girl_file:
            for line in boy_file:
                name, count = line.split()
                boy_names[name] = boy_names.get(name, 0) + int(count)

            for line in girl_file:
                name, count = line.split()
                girl_names[name] = girl_names.get(name, 0) + int(count)

    most_common_boy_name = max(boy_names, key=boy_names.get)
    most_common_girl_name = max(girl_names, key=girl_names.get)

    return most_common_boy_name, most_common_girl_name


# Directory containing the baby names data set
directory = "baby_names_data"  # Replace with the actual directory path

# Prompt the user to enter the time period
start_year = int(input("Enter the start year: "))
end_year = int(input("Enter the end year: "))

# Get the most common names within the specified time period
boy_name, girl_name = get_most_common_names(directory, start_year, end_year)

print(f"The most common boy's name from {start_year} to {end_year} is: {boy_name}")
