#!/usr/bin/env python3 -tt

#Convert the LHS to the RHS using map/filter
lhs = [[1, 3], [4, 2, -5]] #<4,1>
map(sum, lhs)
# Confirmed by list(map(sum, lhs)), need to figure
# out the official method for displaying contents
# of a map.

lhs = [1, True, [2, 3]] # => '1 : True : [2, 3]'
print(" : ".join(map(str, lhs)))
# Clarified in lecture that it's acceptable to use
# non-map operations

def is_positive_int(x):
    return type(x) == int and x > 0

lhs = [0, 1, 0, 6, 'A', 1, 0, 7]
list(filter(is_positive_int, lhs))
