#!/usr/bin/env python3 -tt

import re
import string

def get_vowels_in_order():
    with open('/usr/share/dict/words', 'r') as f:
        words = f.readlines()
    words = map(lambda word: word.rstrip('\n'), words)
    p = re.compile(r'\w*a\w*e\w*i\w*o\w*u\w*')
    return list(filter(lambda w: p.match(w) != None, words))

def regex_crossword_check(horizontal_patterns,
                          vertical_patterns,
                          candidate,
                          alphabet=string.ascii_uppercase):
    hstrings = [''.join(letters) for letters in candidate]
    vstrings = [''.join(letters) for letters in list(zip(*candidate))]
    hstrings_match = all([re.compile(p).match(row)
                          for (p, row)
                          in zip(horizontal_patterns, hstrings)])
    vstrings_match = all([re.compile(p).match(column)
                          for (p, column)
                          in zip(vertical_patterns, vstrings)])
    return hstrings_match and vstrings_match

print(get_vowels_in_order())
horiz = [r'(Y|F)(.)\2[DAF]\1', r'(U|O|I)*T[FRO]+', r'[KANE]*[GIN]*']
vert = [r'(FI|A)+', r'(YE|OT)K', r'(.)[IF]+', r'[NODE]+', r'(FY|F|RG)+']
candidate = [
	['F', 'O', 'O', 'D', 'F'],
	['I', 'T', 'F', 'O', 'R'],
	['A', 'K', 'I', 'N', 'G']
]
regex_crossword_check(horiz, vert, candidate)
