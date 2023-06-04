"""
Exercise 47: Birth Date to Astrological Sign

    The horoscopes commonly reported in newspapers use the position of the sun at the
    time of one’s birth to try and predict the future. This system of astrology divides the
    year into twelve zodiac signs, as outline in the table below:

                    Zodiac sign         Date range
                    ----------------------------------------------
                    Capricorn           December 22 to January 19
                    Aquarius            January 20 to February 18
                    Pisces              February 19 to March 20
                    Aries               March 21 to April 19
                    Taurus              April 20 to May 20
                    Gemini              May 21 to June 20
                    Cancer              June 21 to July 22
                    Leo                 July 23 to August 22
                    Virgo               August 23 to September 22
                    Libra               September 23 to October 22
                    Scorpio             October 23 to November 21
                    Sagittarius         November 22 to December 21

    Write a program that asks the user to enter his or her month and day of birth. Then
    your program should report the user’s zodiac sign as part of an appropriate output
    message.
"""

# User input
month = input("Enter the month of your birth (e.g., January): ")
day = int(input("Enter the day of your birth (e.g., 25): "))
month = month.capitalize()

# Determine the zodiac sign based on the month and day
if (month == "December" and day >= 22) or (month == "January" and day <= 19):
    sign = "Capricorn"
elif (month == "January" and day >= 20) or (month == "February" and day <= 18):
    sign = "Aquarius"
elif (month == "February" and day >= 19) or (month == "March" and day <= 20):
    sign = "Pisces"
elif (month == "March" and day >= 21) or (month == "April" and day <= 19):
    sign = "Aries"
elif (month == "April" and day >= 20) or (month == "May" and day <= 20):
    sign = "Taurus"
elif (month == "May" and day >= 21) or (month == "June" and day <= 20):
    sign = "Gemini"
elif (month == "June" and day >= 21) or (month == "July" and day <= 22):
    sign = "Cancer"
elif (month == "July" and day >= 23) or (month == "August" and day <= 22):
    sign = "Leo"
elif (month == "August" and day >= 23) or (month == "September" and day <= 22):
    sign = "Virgo"
elif (month == "September" and day >= 23) or (month == "October" and day <= 22):
    sign = "Libra"
elif (month == "October" and day >= 23) or (month == "November" and day <= 21):
    sign = "Scorpio"
elif (month == "November" and day >= 22) or (month == "December" and day <= 21):
    sign = "Sagittarius"
else:
    print("Error: Invalid date.")
    exit()

# Display the zodiac sign
print(f"Your zodiac sign is {sign}.")

