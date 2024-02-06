#!/usr/bin/python3

"""Define a class."""

class Square:
    """Define a class Square."""
    def __init__(self, size=0):

        """initialize square
        Args:
            size (int): size of the square
        """
        self.__size = size

    def area(self):
        """calculates the area.

        Returns:
            area.
        """
        return self.__size**2

    @property
    def size(self):
        """int: private size.

        Returns:
            Private size.
        """
        return self.__size
    
    @size.setter
    def size(self, new_size):
        if type(new_size) is not int:
            raise TypeError('size must be an integer')
        elif new_size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = new_size
