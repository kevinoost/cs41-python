#!/usr/bin/env python3 -tt
import itertools

def make_divisibility_test(n):
    def div_by_n(x):
        return x % n == 0
    return div_by_n

def primes_under(n):
    tests = []
    for i in range(2, n):
        if not any(map(lambda test: test(i), tests)):
            tests.append(make_divisibility_test(i))
            yield i

def composites_under(n):
    tests = []
    for i in range(2, n):
        if not any(map(lambda test: test(i), tests)):
            tests.append(make_divisibility_test(i))
        else:
            yield i

def generate_composites():
    tests = []
    for i in itertools.count(2):
        if not any(map(lambda test: test(i), tests)):
            tests.append(make_divisibility_test(i))
        else:
            yield i

# What is the 1000th composite?
comp = generate_composites
for i in range(999):
    next(comp)

next(comp)
# 1197
