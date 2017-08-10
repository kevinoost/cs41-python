#!/usr/bin/env python3 -tt

def generate_triangles():
    total, step = 0, 0
    while True:
        total, step = total + step, step + 1
        yield total

def triangles_under(n):
    for triangle in generate_triangles():
        if triangle >= n:
            break
        print(triangle)
