#!/usr/bin/python3
def print_last_digit(number):
    if number == 0:
        return 0
    elif number > 0:
        LastDigit = number % 10
        return  LastDigit
    elif number < 0:
        LastDigit = abs(number) % 10
        return LastDigit
