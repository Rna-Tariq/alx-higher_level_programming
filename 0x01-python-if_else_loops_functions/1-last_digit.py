#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
LastDigit = number % 10
print("Last digit of", number, "is", end=" ")

if LastDigit == 0:
    print(LastDigit, "and is 0")
elif number > 0 and LastDigit > 5:
    print(LastDigit, "and is greater than 5")
elif number < 0 and LastDigit < 6 and LastDigit != 0:
    LastDigit = abs(number) % 10
    print(-LastDigit, "and is less than 6 and not 0")
