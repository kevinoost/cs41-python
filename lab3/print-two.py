#!/usr/bin/env python3 -tt
"""
File: print-two.py
Program to experiment with, and learn about, passing
arguments to functions.
"""
def print_two(a, b):
    """Summary: print a and b

    Used to experiment with argument-passing.
    """
    print("Arguments: {0} and {1}".format(a, b))

print_two()
# TypeError: print_two() missing 2 required positional arguments: 'a' and 'b'
print_two(4, 1)
# > Arguments: 4 and 1
print_two(41)
# TypeError: print_two() missing 1 required positional argument: 'b'
print_two(a=4, 1)
# SyntaxError: non-keyword arg after keyword arg
print_two(4, a=1)
# TypeError: print_two() got multiple values for argument 'a'
print_two(4, 1, 1)
# TypeError: print_two() takes 2 positional arguments but 3 were given
print_two(b=4, 1)
# SyntaxError: non-keyword arg after keyword arg
print_two(a=4, b=1)
# > Arguments: 4 and 1
print_two(b=1, a=4)
# > Arguments: 4 and 1
print_two(1, a=1)
# print_two() got multiple values for argument 'a'
print_two(4, 1, b=1)
#TypeError: print_two() got multiple values for argument 'b'
print_two(4, b=1)
# > Arguments: 4 and 1
print_two(*[4,1])
# > Arguments: 4 and 1

