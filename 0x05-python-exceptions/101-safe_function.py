#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        x = fct(*args)
        return x
    except Exception as a:
        print("Exception: {}".format(a), file=sys.stderr)
