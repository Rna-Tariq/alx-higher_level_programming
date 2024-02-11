#!/usr/bin/python3
"""Module for add_integer method"""

def add_integer(a, b=98):
    """ Adds two integers
    Args:
    a: first int
    b: second int

    Rasises: 
        TypeError if a or b not int

    Returns: 
        Sum of 2 integers
    """

    if a not in (int, float):
        raise TypeError("Please enter a numer")
    if b not in (int, float):
        raise TypeError("Please enter a numer")
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
