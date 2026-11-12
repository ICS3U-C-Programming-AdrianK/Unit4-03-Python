#!/usr/bin/env python3
# created by : Adrian student
# Date : 11th NOV 2026
# This programs asks the user to enter a positive integer
# it then uses a for loop to calculate and display the
# “square” (power of 2) starting from 0 until this number then it


def main():
    # get the user number as a string
    user_number_str = input("Enter a positive integer : ")

    try:
        # cast the user number fom string to integer
        user_number_int = int(user_number_str)
        if user_number_int >= 0:
            for counter in range(user_number_int + 1):
                power_of_two = counter**2
                print(f"{counter}² = {power_of_two}")
        else:
            print(f"{user_number_int} is not a positive number")
    except:
        print(f"{user_number_str} is not an integer")


if __name__ == "__main__":
    main()
