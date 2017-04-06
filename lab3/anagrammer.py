#!/usr/bin/env python3 -tt
"""
File: anagrammer.py

Given a word, find all anagrams of that word
"""
with open('/usr/share/dict/words', 'r') as f:
    lines = f.readlines()

words = {word.lower().strip() for word in lines}
letters = input("Letters? ").lower()
sorted_letters = ''.join(sorted(letters))
anagrams = []

for word in words:
    sorted_word = ''.join(sorted(word))
    if sorted_letters == sorted_word:
        anagrams.append(word)

print(anagrams)
