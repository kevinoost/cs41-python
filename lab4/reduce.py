import operator
from functools import reduce

"""
Use the reduce function to find the least 
common multiple of a arbitrary list of arguments.
This can be accomplished in one line of Python.
"""

def gcd(a, b):
    """Reference implementation of finding the
    greatest common denominator of two numbers"""
    while b != 0:
        a, b = b, a % b
    return a

# Note: I'm fairly confident this is correct, but not 100%
def lcm(*args):
    return reduce(
        lambda x, y:
        x if x % y == 0
        else (x*y) // gcd(x, y),
        args,1)

# Use reduce in conjunction with a function from the
# operator module to compute factorials in one line of
# Python:

def fact(n):
    return reduce(operator.mul, range(1,n+1), 1)


