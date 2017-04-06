#!/usr/bin/env python3 -tt
"""
File: triangle-numbers.py

The nth term of the sequence of triangle numbers
 is given by 1 + 2 + ... + n = n(n+1) / 2. For
 example, the first ten triangle numbers are: 

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number 
corresponding to its alphabetical position and
adding these values we form a word value. For
example, the word value for SKY is:
19 + 11 + 25 = 55 and 55 is a triangle number.
 If the word value is a triangle number then 
we shall call the word a triangle word.

Using either /usr/share/dict/words or 
http://stanfordpython.com/words, a 2.5M text
file containing over 200 thousand English words,
which are triangle words? As a sanity check, we
found 16303 distinct triangle words.

Hint: you can use ord(ch) to get the integer
ASCII value of a character
"""

triangle_numbers = [x*(x+1)//2 for x in range(40)]

def get_alphabetical_order(char):
    if 'a' <= char <= 'z':
        return ord(char) - ord('a') + 1
    return ord(char) - ord('A') + 1

def get_word_sum(word):
    return sum([get_alphabetical_order(char) for char in word])

with open('/usr/share/dict/words', 'r') as f:
    lines = f.readlines()

distinct_words = {word.lower() for word in lines}


print(len([word for word in distinct_words
           if (get_word_sum(word.strip()) in triangle_numbers)]))
