"""
Exercise 174: Run-Length Encoding

    Write a recursive function that implements the run-length compression technique
    described in Exercise 173. Your function will take a list or a string as its only para-
    meter. It should return the run-length compressed list as its only result. Include a main
    program that reads a string from the user, compresses it, and displays the run-length
    encoded result.

    Hint:You may want to include a loop inside the body of your recursive function.
"""


def encode_run_length(data):
    if not data:  # Base case: empty list or string
        return []

    count = 1
    compressed = []
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            compressed.append(data[i - 1])
            compressed.append(count)
            count = 1

    # Add the last element and its count
    compressed.append(data[-1])
    compressed.append(count)

    return compressed


def main():
    input_data = input("Enter a string: ")
    encoded_list = encode_run_length(input_data)

    print("Original Input:", input_data)
    print("Encoded List:", encoded_list)


# Run the main program
main()


