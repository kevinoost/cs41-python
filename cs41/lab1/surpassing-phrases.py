#!/usr/bin/env python3 -tt
"""
File: surpassing-phrases.py
"""
def is_surpassing_word(word):
    gaps = [abs(ord(x)-ord(y)) for (x,y) in zip(word[:],word[1:])]
    differences = [x-y for (x,y) in zip(gaps,gaps[1:]+[0])]
    return all(x < 0 for x in differences[:-1])

def is_surpassing_phrase(phrase):
    return all(is_surpassing_word(word) for word in phrase.split())

