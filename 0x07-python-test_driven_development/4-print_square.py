#!/usr/bin/python3
"""
This function prints a square with the character #

"""

def print_square(size):
    """This function accepts one argument of type int or float
     and prints out the square

     Args:
        size: The length of the square of type int

     Raise:
        TypeError: size must be an integer
        ValueError: size must be >= 0

    """

    if not isinstance(size, (int, float)) \
            or (isinstance(size, float) and int(size < 0)):
        raise TypeError("size must be an integer")
    else:
        if int(size) < 0:
            raise ValueError("size must be >= 0")
        else:
            for i in range(int(size)):
                print('#' * int(size))
