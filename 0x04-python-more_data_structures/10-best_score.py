#!/usr/bin/python3
def best_score(a_dictionary):
    score = 0
    best_key = "None"

    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return best_key

    for i, j in a_dictionary.items():
        if j > score:
            score = j
            best_key = i
    return best_key
