#!/usr/bin/python3

"""
This function that returns the list of available
attributes and methods of an object
"""


def lookup(obj):
    """This returns attributes amd methods of an object

    Args:
        obj: The object
        Return: The attributes and the methods of an object
    """

    return dir(obj)

