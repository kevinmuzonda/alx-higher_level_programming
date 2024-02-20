#!/usr/bin/python3

""""
This function tahat returns True if the object is exactly an
instance of the specified class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """Defining the function

        Args:
        obj: The object to check
        a_class: The specified class

    Return:
        True: If obj is an instance
        False: If otherwise
    """
    return isinstance(obj, a_class)
