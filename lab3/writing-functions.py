#!/usr/bin/env python3 -tt

def speak_excitedly(message, exclamations=1, capitalize=False):
    if capitalize:
        message = message.upper()
    print("{}{}".format(message,"!"*exclamations))

speak_excitedly("I love Python")
speak_excitedly("Keyword arguments are great", exclamations=4)
speak_excitedly("I guess Ruby is okay...", exclamations=0)
speak_excitedly("Let's go Bama", exclamations=2, capitalize=True)

def average(*nums):
    if len(nums) == 0:
        return None
    return sum(nums) / len(nums)

average()  # => None
average(5) # => 5.0
average(6, 8, 9, 11)  # => 8.5

