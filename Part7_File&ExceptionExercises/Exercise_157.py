"""
Exercise 157: Distinct Names

    In this exercise, you will create a program that reads every file in the baby names data
    set described in Exercise 154. As your program reads the files, it should keep track
    of each name used for a boy and each name used for a girl. Your program should
    output two lists. One list will contain all of the names that have been used for girls.
    The other list will contain all of the names that have been used for boys. Neither of
    your lists should contain any repeated values.
"""
import os


def get_distinct_names(directory):
    boy_names = set()
    girl_names = set()

    for filename in os.listdir(directory):
        if filename.endswith("_BoysNames.txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, "r") as file:
                for line in file:
                    name, _ = line.split()
                    boy_names.add(name)
        elif filename.endswith("_GirlsNames.txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, "r") as file:
                for line in file:
                    name, _ = line.split()
                    girl_names.add(name)

    return list(boy_names), list(girl_names)


# Directory containing the baby names data set
directory = "baby_names_data"  # Replace with the actual directory path

# Get the distinct names for boys and girls
boy_names, girl_names = get_distinct_names(directory)

print("Distinct boy names:")
for name in boy_names:
    print(name)

print("\nDistinct girl names:")
for name in girl_names:
    print(name)
