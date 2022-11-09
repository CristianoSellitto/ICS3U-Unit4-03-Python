#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in October 2022
# A program that finds the square roots of integers


def main():
    # Finds the square roots of integers

    number = input("Enter a positive integer to square root: ")
    try:
        floating_point_number = float(number)
        integer = int(number)
        if integer > 0 and integer == floating_point_number:
            print("")
            for counter in range(integer + 1):
                answer = counter * counter
                print("{0}² = {1}".format(counter, answer))
        elif integer == 0 and integer == floating_point_number:
            print("\n0² = 0")
        else:
            print("\n{} is an incompatible integer.".format(integer))
    except ValueError:
        print("\nError: {} is not an integer.".format(number))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
