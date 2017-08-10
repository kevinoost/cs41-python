#!/usr/bin/env python3 -tt
"""
File: triad-phrase.py
"""
with open('/usr/share/dict/words', 'r') as f:
    lines = f.readlines()

words = {word.lower().strip() for word in lines}

def is_triad_word(word):
    word = word.lower()
    return (word[::2] in words) and (word[1::2] in words)

def is_triad_phrase(phrase):
    for word in phrase.split():
        if not is_triad_word(word):
            return False
    return True

