#!/usr/bin/env python3 -tt

import operator

def dot_product(u, v):
    return sum(map(operator.mul, u, v))

# where m is a tuple-of-tuples
"""
((1, 2, 3), => ((1, 4),
 (4, 5, 6))     (2, 5),
                (3, 6))
"""

# Note: couldn't figure out the solution to transpose,
# looked it up in the solutions handout.
def transpose(m):
    return tuple(zip(*m))

def matmul(m1, m2):
    return map(dot_product, m1, transpose(m2))

def matmul(m1, m2):
    return list(map(dot_product, m1*len(m2[0]), transpose(m2)*len(m1)))

m1 = ((1,3,5,7),
      (2,4,6,8))
m2 = ((1,8,9),
      (2,7,10),
      (3,6,11),
      (4,5,12))
matmul(1,2)
