"""
Exercise 93: Next Prime

    In this exercise you will create a function named nextPrime that finds and returns
    the first prime number larger than some integer, n. The value of n will be passed to
    the function as its only parameter. Include a main program that reads an integer from
    the user and displays the first prime number larger than the entered value. Import
    and use your solution to Exercise 92 while completing this exercise.
"""


def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def nextPrime(n):
    prime = n + 1
    while True:
        if is_prime(prime):
            return prime
        prime += 1


def main():
    num = int(input("Enter an integer: "))
    prime = nextPrime(num)
    print(f"The first prime number larger than {num} is: {prime}")


if __name__ == '__main__':
    main()
