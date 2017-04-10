#!/usr/bin/env python3 -tt

"""
Python defaults to ordering sequences by a default 
ordering. For instances, strings sort alphabetically, 
and tuples sort lexicographically. Sometimes, however, 
we need to sort based on a custom key value. In Python,
we can supply an optional key argument to sorted(seq),
max(seq), min(seq), and seq.sort() to determine the 
values used for ordering elements in a sequence. In 
Python, these default sorting tools are guaranteed to 
be stable.
"""

words = ['pear', 'cabbage', 'apple', 'bananas']
min(words)  # => 'apple', as predicted
words.sort(key=lambda s: s[-1])
# Alternatively, key=operator.itemgetter(-1)
words  # => ['cabbage', 'apple', 'pear', 'bananas'] ...
# Why 'cabbage' > 'apple'?
# A: Because Python uses a stable sort that preserves relative
#    ordering in the event of a 'tie', and 'cabbage' preceded
#    apple in the list given to the function.
max(words, key=len)
# Q: 'cabbage' ... Why not 'bananas'?
# A: Again, because Python uses a stable sort that preserves
#    relative ordering in the event of a 'tie'.
min(words, key=lambda s: s[1::2])  # What will this value be?
# Prediction: 'bananas'. Prediction was correct.

"""
Write a function to return the two words with
the highest alphanumeric score of uppercase 
letters:
"""
def alpha_score(upper_letters):
    """Computers the alphanumeric sum of letters in a string.
    Prerequisite: upper_letters is composed entirely of capital letters.
    """
    return sum(map(lambda l: 1 + ord(l) - ord('A'), upper_letters))

alpha_score('ABC')  # => 6 = 1 ('A') + 2 ('B') + 3 ('C')
"""
def two_best(words):
    words.sort(key=lambda s: alpha_score(s.upper()), reverse=True)
    if len(words) >= 2:
        return words[0], words[1]
"""

# Note: concise, but probably not readable
def two_best_first_attempt(words):
    words.sort(key=lambda s: alpha_score(
        ''.join(filter(lambda char: ord('A') <= ord(char) <= ord('Z'), s))),
        reverse=True)
    if len(words) >= 2:
        return words[0], words[1]

def get_upper(s):
    return ''.join(filter(lambda char: ord('A') <= ord(char) <= ord('Z'), s))

# Second attempt: hopefully clearer:
def two_best(words):
    words.sort(key=lambda word: alpha_score(get_upper(word)),
               reverse=True)
    if len(words) >= 2:
        return words[0], words[1]

print(two_best(['hEllO', 'wOrLD', 'i', 'aM', 'PyThOn']))

"""
Result is: ('PyThOn', 'wOrLD')

Note: the result of

list(map(lambda x: (x, alpha_score(get_upper(x))), 
         ['hEllO', 'wOrLD', 'i', 'aM', 'PyThOn']))

is:

[('hEllO', 20), ('wOrLD', 31), ('i', 0), ('aM', 13), ('PyThOn', 51)]

which confirms the correctness of our result for two_best(...)

An even better solution (after peeking at the solutions) is:

def two_best(words):
    words.sort(key=lambda word: alpha_score(filter(str.isupper, word)),
               reverse=True)
    if len(words) >= 2:
        return words[0], words[1]

"""

def two_best(words):
    words.sort(key=lambda word: alpha_score(filter(str.isupper, word)),
               reverse=True)
    return words[:2]
