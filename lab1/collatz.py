sho#!/usr/bin/env python3
"""
File: collatz.py

Problem Description:
The Collatz sequence is an iterative sequence defined on the positive integers by:

n -> n / 2    if n is even
n -> 3n + 1   if n is odd

The sequence terminates if/when n equals 1.

Using the rule above and starting with 13 yields the sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

Which we call a ``chain'' of length 10.

What is the length of the longest chain which has a starting number under 1000?

Challenge: Same question, but for any starting number under 1,000,000 (you may need to implement a cleverer-than-naive algorithm)

Note: There's still room for further optimization. Current solution does not cache every collatz computation it performs. There's is a superior recursive solution.

======================================================================

Solution: I took a dynamic programming approach with the following results:

(n=1000) 194
(n=1000000) 557

The 1,000,000 case took about three seconds to compute on my laptop.
"""

collatz_lengths = {}

def get_collatz_length(n_argument):
    num_steps = 1
    n = n_argument
    while (n != 1):
        if n in collatz_lengths:
            num_steps = num_steps + collatz_lengths[n]
            break
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3*n + 1
        num_steps = num_steps + 1
    collatz_lengths[n_argument] = num_steps
    return num_steps

def get_max_chain(n):
    return max([get_collatz_length(x) for x in range(1,n)])

print(get_max_chain(1000))
print(get_max_chain(1000000))
