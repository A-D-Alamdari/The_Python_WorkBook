"""
Exercise 88: Is it a Valid Triangle?

    If you have 3 straws, possibly of differing lengths, it may or may not be possible
    to lay them down so that they form a triangle when their ends are touching. For
    example, if all of the straws have a length of 6 inches. then one can easily construct
    an equilateral triangle using them. However, if one straw is 6 inches. long, while the
    other two are each only 2 inches. long, then a triangle cannot be formed. In general,
    if any one length is greater than or equal to the sum of the other two then the lengths
    cannot be used to form a triangle. Otherwise they can form a triangle.
    Write a function that determines whether or not three lengths can form a triangle.
    The function will take 3 parameters and return a Boolean result. In addition, write a
    program that reads 3 lengths from the user and demonstrates the behaviour of this
    function.
"""


def is_triangle(a, b, c):
    if a >= b + c or b >= a + c or c >= a + b:
        return False
    else:
        return True


def main():
    a = float(input("Enter the length of the first side: "))
    b = float(input("Enter the length of the second side: "))
    c = float(input("Enter the length of the third side: "))

    if is_triangle(a, b, c):
        print("Yes, a triangle can be formed.")
    else:
        print("No, a triangle cannot be formed.")


if __name__ == '__main__':
    main()
