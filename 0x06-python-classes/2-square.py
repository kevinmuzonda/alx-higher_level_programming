#!/usr/bin/python3
""" defines a class named Square """


class Square:
    """ defines a function named __init__ """
    def __init__(self, size=0):
        """ if statement """
        if type(size) is not int:
            raise TypeError("size must be an integer")
            """ TypeError: if size is not an integer"""
        if size < 0:
            raise ValueError("size must be >= 0")
            """ValueError: if size is less than zero"""
        self.__size = size
