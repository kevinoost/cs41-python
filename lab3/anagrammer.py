#!/usr/bin/env python3 -tt
"""
File: anagrammer.py

Given a word, find all anagrams of that word

TODO: Experiment to see which method is faster
for different test cases. I'm guessing 2 is
much faster.
"""
import itertools

with open('/usr/share/dict/words', 'r') as f:
    lines = f.readlines()
words = {word.lower().strip() for word in lines}

def find_anagrams_1():
    letters = input("Letters? ").lower()
    sorted_letters = ''.join(sorted(letters))
    anagrams = []
    
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_letters == sorted_word:
            anagrams.append(word)
    
    print(anagrams)

def find_anagrams_2():
    letters = input("Letters? ").lower()
    permutations = map(lambda lettertuple: ''.join(lettertuple), itertools.permutations(letters, len(letters)))
    anagrams = filter(lambda permutation: permutation in words, permutations)
    print(list(anagrams))

if __name__ == '__main__':
    find_anagrams_2()
