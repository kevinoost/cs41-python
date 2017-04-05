#!/usr/bin/env python3
"""
File: fizzbuzzfizzbuzz.py

Problem: Find the sum of all the multiples of 3 or 5 below 1001.
"""

def sum_all_3s_and_5s_under_n(n):
    return sum([x for x in range(n) if (x % 3 == 0) or (x % 5 == 0)])

print(sum_all_3s_and_5s_under_n(1001))
