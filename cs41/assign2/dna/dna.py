#!/usr/bin/env python3 -tt
"""
File: dna.py
------------
Assignment 2: Quest for the Holy Grail
Course: CS 41
Name: <YOUR NAME>
SUNet: <SUNet ID>

Replace this with a description of the program.
"""

def min_distance(start, end):
	"""Return the Levenshtein distance between two strings.

	You can change the function signature if you'd like, in order
	to implement caching or any other clever tricks you'd like.

	@param start, end: strings to find the edit distance between
	@return: minimum number of edits to turn start into end
	"""
	pass


if __name__ == '__main__':
	"""
	TODO
	(1) Reads DNA strands from a file formatted as:
			startSequence1	endSequence1
			startSequence2	endSequence2
			...
			startSequenceN	endSequenceN
		Each start/end pair is on its own line, and the start and end strands
		are separated by a tab.
	(2) Compute minimum edit distance between each pair.
	(3) Output the total number of edits required for all DNA transformations
	    in the file. Use this as the key from the next part of the assignment.
	"""
	DATA_FILE = 'dna-small.txt'
	# Read DNA strands from file

	# Use the min_distance function to compute the edit distance for each pair

	# Output the total number of edits

