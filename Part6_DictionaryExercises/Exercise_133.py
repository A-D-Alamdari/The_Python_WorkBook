"""
Exercise 133:Write Out Numbers in English

    While the popularity of cheques as a payment method has diminished in recent years,
    some companies still issue them to pay employees or vendors. The amount being
    paid normally appears on a cheque twice, with one occurrence written using digits,
    and the other occurrence written using English words. Repeating the amount in two
    different forms makes it much more difficult for an unscrupulous employee or vendor
    to modify the amount on the cheque before depositing it.
    In this exercise, your task is to create a function that takes an integer between 0 and
    999 as its only parameter, and returns a string containing the English words for that
    number. For example, if the parameter to the function is 142 then your function should
    return “one hundred forty two”. Use one or more dictionaries to implement
    your solution rather than large if/elif/else constructs. Include a main program that
    reads an integer from the user and displays its value in English words.
"""


def number_to_words(number):
    # Define dictionaries for mapping numbers to words
    ones = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
    }
    tens = {
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
        14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
        18: 'eighteen', 19: 'nineteen'
    }
    multiples_of_10 = {
        20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
        60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'
    }

    # Handle special cases
    if number < 10:
        return ones[number]
    elif number < 20:
        return tens[number]
    elif number < 100:
        tens_digit = number // 10 * 10
        ones_digit = number % 10
        if ones_digit == 0:
            return multiples_of_10[tens_digit]
        else:
            return multiples_of_10[tens_digit] + ' ' + ones[ones_digit]
    elif number < 1000:
        hundreds_digit = number // 100
        remaining_number = number % 100
        if remaining_number == 0:
            return ones[hundreds_digit] + ' hundred'
        else:
            return ones[hundreds_digit] + ' hundred ' + number_to_words(remaining_number)
    else:
        return 'Number out of range'


# Example usage
user_input = int(input("Enter a number between 0 and 999: "))
result = number_to_words(user_input)
print(result)
