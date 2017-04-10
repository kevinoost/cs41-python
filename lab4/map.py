#!/usr/bin/env python3 -tt

# For each of the following rows, write a
# single statement using map that converts
# the left column into the right column:

#  ['12', '-2', '0'] => [12, -2, 0]
list(map(int, ['12', '-2', '0']))
# ['hello', 'world'] => [5, 5]
list(map(len, ['hello', 'world']))
# ['hello', 'world'] => ['olleh', 'dlrow']
list(map(lambda s: s[::-1], ['hello', 'world']))
# range(2,6) => [(2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125)]
list(map(lambda x: (x, x**2, x**3), range(2, 6)))
# zip(range(2, 5), range(3, 9, 2)) => [6, 15, 28]
list(map(lambda tup: tup[0] * tup[1], zip(range(2, 5), range(3, 9, 2))))

""" Note: the text below is here to just remind me
of this cool feature.

Using Multiple Iterables

The map function can accept a variable number of 
iterables as arguments. Thus, 

map(func, iterA, iterB, iterC) 

is equivalent to 

map(func, zip(iterA, iterB, iterC)).

This can be used as follows:

map(int, ('10110', '0xCAFE', '42'), (2, 16, 10))  

# generates 22, 51966, 42

This works because int takes an optional second
argument specifying the conversion base!
"""

