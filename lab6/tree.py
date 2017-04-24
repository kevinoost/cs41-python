#!/usr/bin/env python3 -tt

"""
This is extremely ugly, but it works
"""


import sys
import pathlib

p = pathlib.Path.cwd()
if len(sys.argv) > 1:
    directory = sys.argv[1]
    p = pathlib.Path(sys.argv[1])
p = pathlib.Path('/Users/jamesshapiro/Desktop/cs41')


def is_last(element, array):
    return element == array[-1]

already_visited = []


def print_contents(path, n_levels=0, is_last_item=False):
    if n_levels == 0:
        print(p.name)
    else:
        if is_last_item:
            print ('{}{}── {}'.format('    ' * (n_levels - 1), "└", path.name))
        else:
            print('{}{}── {}'.format('    ' * (n_levels - 1), "├", path.name))
    items = [x for x in path.iterdir()]
    for item in items:
        if item.is_file():
            if '.DS_Store' in item.name:
                continue
            if is_last(item, items):
                print ('{}{}── {}'.format('    ' * n_levels, "└", item.name))
            else:
                print ('{}{}── {}'.format('    ' * n_levels, "├", item.name))
        else:
            if item not in already_visited and not 'git' in item.name:
                already_visited.append(item)
                print_contents(item, n_levels+1, is_last(item, items))

print_contents(p, 0, False)
