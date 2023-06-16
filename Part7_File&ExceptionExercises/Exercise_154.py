"""
Exercise 154: Names that Reached Number One

    The baby names data set consists of over 200 files. Each file contains a list of 100
    names, along with the number of times each name was used. There are two files for
    each year: one containing names used for girls and the other containing names used
    for boys. The data set includes data for every year from 1900 to 2012.
    Write a program that reads every file in the data set and identifies all of the names
    that were most popular in at least one year. Your program should output two lists:
    one containing the most popular names for boys and the other containing the most
    popular names for girls. Neither of your lists should include any repeated values.
"""

import os

import os

import os


def get_most_popular_names(directory):
    popular_boy_names = set()
    popular_girl_names = set()

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            year = int(filename.split("_")[0])
            with open(os.path.join(directory, filename), "r") as file:
                lines = file.readlines()
                boy_names = []
                girl_names = []
                for line in lines:
                    name, count = line.strip().split()
                    count = int(count)
                    if count > 0:
                        boy_names.append((name, count))
                        girl_names.append((name, count))
                boy_names.sort(key=lambda x: x[1], reverse=True)
                girl_names.sort(key=lambda x: x[1], reverse=True)
                popular_boy_names.add(boy_names[0][0])
                popular_girl_names.add(girl_names[0][0])

    return popular_boy_names, popular_girl_names


# Directory containing the baby names data set
directory = "baby_names_data"  # Replace with the actual directory path
boy_names, girl_names = get_most_popular_names(directory)

# Display the most popular names for boys
print("Most popular names for boys:")
for name in boy_names:
    print(name)

# Display the most popular names for girls
print("\nMost popular names for girls:")
for name in girl_names:
    print(name)
