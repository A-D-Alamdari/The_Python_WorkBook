"""
Exercise 132: Postal Codes

    In a Canadian postal code, the first, third and fifth characters are letters while the
    second, fourth and sixth characters are numbers. The province can be determined
    from the first character of a postal code, as shown in the following table. No valid
    postal codes currently begin with D, F, I, O, Q, U, W, or Z.

                Province                First character(s)
                ------------------------------------------
                Newfoundland            A
                Nova Scotia             B
                Prince Edward Island    C
                New Brunswick           E
                Quebec                  G, H and J
                Ontario                 K, L, M, N and P
                Manitoba                R
                Saskatchewan            S
                Alberta                 T
                British Columbia        V
                Nunavut                 X
                Northwest Territories   X
                Yukon                   Y

    The second character in a postal code identifies whether the address is rural or
    urban. If that character is a 0 then the address is rural. Otherwise it is urban.
    Create a program that reads a postal code from the user and displays the province
    associated with it, along with whether the address is urban or rural. For example,
    if the user enters T2N 1N4 then your program should indicate that the postal code
    is for an urban address in Alberta. If the user enters X0A 1B2 then your program
    should indicate that the postal code is for a rural address in Nunavut or Northwest
    Territories. Use a dictionary to map from the first character of the postal code to the
    province name. Display a meaningful error message if the postal code begins with
    an invalid character.
"""


def get_province(postal_code):
    province_mapping = {
        'A': 'Newfoundland',
        'B': 'Nova Scotia',
        'C': 'Prince Edward Island',
        'E': 'New Brunswick',
        'G': 'Quebec',
        'H': 'Quebec',
        'J': 'Quebec',
        'K': 'Ontario',
        'L': 'Ontario',
        'M': 'Ontario',
        'N': 'Ontario',
        'P': 'Ontario',
        'R': 'Manitoba',
        'S': 'Saskatchewan',
        'T': 'Alberta',
        'V': 'British Columbia',
        'X': 'Nunavut or Northwest Territories',
        'Y': 'Yukon'
    }

    first_char = postal_code[0].upper()

    if first_char in province_mapping:
        province = province_mapping[first_char]
        if postal_code[1] == '0':
            address_type = 'rural'
        else:
            address_type = 'urban'

        return f"The postal code is for an {address_type} address in {province}."
    else:
        return "Invalid postal code."


# Example usage
user_input = input("Enter a Canadian postal code: ")
result = get_province(user_input)
print(result)
