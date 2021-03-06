#!/usr/bin/env python3 -tt
"""
File: generate-pascal-row.py

Write a function that generates the next level
of Pascal’s triangle given a list that represents
a valid row of Pascal’s triangle.

generate_pascal_row([1, 2, 1]) -> [1, 3, 3, 1]
generate_pascal_row([]) -> [1]
generate_pascal_row([1, 4, 6, 4, 1]) -> [1, 5, 10, 10, 5, 1]

"""
def generate_pascal_row(prev_row):
    if len(prev_row) == 0:
        return [1]
    return [x+y for (x,y) in zip(prev_row + [0], [0] + prev_row)]

