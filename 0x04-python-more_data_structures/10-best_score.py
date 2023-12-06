#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        score = max(list(a_dictionary.values()))
        for i in a_dictionary:
            if a_dictionary[i] == score:
                return i
    return None
