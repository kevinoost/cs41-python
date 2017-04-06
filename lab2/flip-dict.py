#!/usr/bin/env python3 -tt

"""
File: flip-dict.py

Write a function that properly reverses the keys and 
values of a dictionary - each key (originally a value) 
should map to a set of values (originally keys) that 
mapped to it. For example,

flip_dict({"CA": "US", "NY": "US", "ON": "CA"})
# => {"US": {"CA", "NY"}, "CA": {"ON"}}
"""

def flip_dict(orig_dict):
    return {value: [k for k, v in orig_dict.items() if v == value]
            for value in orig_dict.values()}
