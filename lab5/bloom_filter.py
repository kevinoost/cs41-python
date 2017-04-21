#!/usr/bin/env python3 -tt
import hashlib

class BloomFilter:
    def __init__(self, num_array_entries=2343710, num_hash_functions=5):
        self.num_array_entries = num_array_entries
        self.entries = [False] * num_array_entries
        self.hash_functions = [hashlib.sha1()]
#        self.hash_functions = [hashlib.sha1(), hashlib.sha224(), hashlib.sha256(), hashlib.sha384(), hashlib.sha512()]
    def get_entry(self, element, hash_function):
        m = hash_function.copy()
        m.update(element.encode('utf-8'))
        int_entry = int(m.hexdigest(), 16)
        return int_entry % self.num_array_entries
    def insert(self, element):
        for hash_function in self.hash_functions:
            entry = self.get_entry(element, hash_function)
            self.entries[entry] = True
    def __contains__(self, element):
        entries = []
        for hash_function in self.hash_functions:
            entry_idx = self.get_entry(element, hash_function)
            entry = self.entries[entry_idx]
            entries.append(entry)
        return all(entries)
"""        return all(
            [self.entries[self.get_entry(element, hash_function)] for hash_function in self.hash_functions])"""

bf = BloomFilter()
with open('/usr/share/dict/words', 'r', encoding='utf-8') as f:
    lines = f.readlines()
lines = [x.lower().rstrip() for x in lines]
for word in lines:
    bf.insert(word)

