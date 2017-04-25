#!/usr/bin/env python3 -tt

import itertools

def tabulate(f, start=0, step=1):
    return map(f, itertools.count(start, step))

sqgen = tabulate(lambda x: x ** 2)

next(sqgen)
next(sqgen)
next(sqgen)
next(sqgen)
