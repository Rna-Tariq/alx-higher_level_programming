#!/usr/bin/python3
def uppercase(input_str):
    for char in input_str:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - (ord('a') - ord('A')))
        else:
            uppercase_char = char

        print("{}".format(uppercase_char), end='')

    print()
