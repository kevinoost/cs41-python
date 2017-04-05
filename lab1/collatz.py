#!/usr/bin/env python3
"""
File: collatz.py
"""

def get_collatz_length(n):
    num_steps = 0
    while (n != 1):
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3*n + 1
        num_steps = num_steps + 1
    return num_steps

def get_max_chain(n):
    return max([get_collatz_length(x) for x in range(1,n)])

print(get_max_chain(1000))
