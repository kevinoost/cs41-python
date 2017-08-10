#!/usr/bin/env python3 -tt

"""
Filter

Recall from class that filter(pred, iterable) keeps 
only those elements from an iterable that satisfy 
a predicate function.

Write statements using filter that convert the 
following sequences from the left column to the
right column:
"""

#['12', '-2', '0'] => ['12', '0']
list(filter(lambda x: int(x) >= 0, ['12', '-2', '0']))
#['hello', 'world']	['world']
list(filter(lambda x: x in 'world peace', ['hello', 'world']))
#['Stanford', 'Cal', 'UCLA'] => ['Stanford']
list(filter(lambda x: len(x) > 4, ['Stanford', 'Cal', 'UCLA']))
#range(20)	[0, 3, 5, 6, 9, 10, 12, 15, 18]
list(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(20)))
