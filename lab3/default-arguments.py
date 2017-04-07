#!/usr/bin/env python3 -tt
"""
File: default-arguments.py
"""
def keyword_args(a, b=1, c='X', d=None):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)

keyword_args(5)
# a: 5
# b: 1
# c: X
# d: None

keyword_args(a=5)
# (same as above)

keyword_args(5, 8)
# a: 5
# b: 8
# c: X
# d: None

keyword_args(5, 2, c=4)
# a: 5
# b: 2
# c: 4
# d: None

keyword_args(5, 0, 1)
# a: 5
# b: 0
# c: 1
# d: None

keyword_args(5, 2, d=8, c=4)
# a: 5
# b: 2
# c: 4
# d: 8

keyword_args(5, 2, 0, 1, "")
# TypeError: keyword_args() takes from 1 to 4 positional arguments
# but 5 were given

keyword_args(c=7, 1)
#SyntaxError: non-keyword arg after keyword arg

keyword_args(c=7, a=1)
# a: 1
# b: 1
# c: 7
# d: None

keyword_args(5, 2, [], 5)
# prints arguments as expected

keyword_args(1, 7, e=6)
# TypeError: keyword_args() got an unexpected keyword argument 'e'

keyword_args(1, c=7)
# prints arguments as expected

keyword_args(5, 2, b=4)
#TypeError: keyword_args() got multiple values for argument 'b'

keyword_args(b=1, c=2, d=3)
#TypeError: keyword_args() missing 1 required positional argument: 'a'

keyword_args(*[1,2,3,4])
# prints arguments as expected
