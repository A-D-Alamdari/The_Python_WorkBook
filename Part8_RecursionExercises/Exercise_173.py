"""
Exercise 173: Run-Length Decoding

    Run-length encoding is a simple data compression technique that can be effec-
    tive when repeated values occur at adjacent positions within a list. Compression is
    achieved by replacing groups of repeated values with one copy of the value, followed
    by the number of times that the value should be repeated. For example, the list ["A",
    "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B",
    "B", "B", "A", "A", "A", "A", "A", "A", "B"] would be compressed
    as ["A", 12, "B", 4, "A", 6, "B", 1]. Decompression is performed by
    replicating each value in the list the number of times indicated.
    Write a recursive function that decompresses a run-length encoded list. Your
    recursive function will take a run-length compressed list as its only parameter. It will
    return the decompressed list as its only result. Create a main program that displays
    a run-length encoded list and the result of decoding it.
"""


def decode_run_length(encoded_list):
    if not encoded_list:  # Base case: empty list
        return []

    if len(encoded_list) >= 2 and isinstance(encoded_list[0], int):
        count = encoded_list[0]
        value = encoded_list[1]
        return [value] * count + decode_run_length(encoded_list[2:])
    else:
        return [encoded_list[0]] + decode_run_length(encoded_list[1:])


# Test the decoding function
encoded_list = ["A", 12, "B", 4, "A", 6, "B", 1]
decoded_list = decode_run_length(encoded_list)

# Display the original encoded list and the decoded list
print("Encoded List:", encoded_list)
print("Decoded List:", decoded_list)

