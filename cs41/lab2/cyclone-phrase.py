#!/usr/bin/env python3 -tt

"""
File: cyclone-phrase.py

Cyclone words are words that have a sequence of 
characters in alphabetical order when following 
a cyclic pattern.

For example, "adjourned"
+---------------+
| +-----------+ |
| | +-------+ | |
| | | +---+ | | |
| | | |   | | | |
| | | |   v v v v
a d j o u r n e d
  ^ ^ ^ ^ | | | |
  | | | | | | | |
  | | | +-+ | | |
  | | +-----+ | |
  | +---------+ |
  +-------------+

Write a function to determine whether an entire 
phrase passed into a function is made of cyclone 
words. You can assume that all words are made of
only alphabetic characters, and are separated by
whitespace.
"""

def is_cyclone_word(word):
    reverse_word = word[::-1]
    reverse_word_prepended = 'a' + reverse_word
    for i in range((len(word)-1)//2):
        if word[i] > reverse_word[i] or reverse_word_prepended[i] > word[i]:
            return False
    return True

def is_cyclone_phrase(phrase):
    for word in phrase.split():
        if not is_cyclone_word(word):
            return False
    return True
