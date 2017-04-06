#!/usr/bin/env python3 -tt

"""
File: gcd.py
Find the greatest common divisor of two numbers (a, b), where a < b

e.g.:

gcd(10, 25) # => 5
gcd(14, 15) # => 1
gcd(3, 9) # => 3
gcd(1, 1) # => 1
"""

def gcd(a, b):
    while b % a > 0:
        (a, b) = (b % a, a)
    return a

def gcd_clever(a, b):
    a if b % a == 0 else gcd(b % a, a)
