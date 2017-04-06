#!/usr/bin/python
"""
File: hello.py

[0, 1, 2, 3] -> [1, 3, 5, 7]

[3, 5, 9, 8] -> [True, False, True, False]

["TA_sam", "TA_guido", "student_poohbear", "student_htiek"]
    -> ["sam", "guido"]

['apple', 'orange', 'pear'] -> ['A', 'O', 'P']

['apple', 'orange', 'pear'] -> ['apple', 'pear']

['apple', 'orange', 'pear'] -> [('apple', 5), ('orange', 6), ('pear', 4)]

['apple', 'orange', 'pear'] -> {'apple': 5, 'orange': 6, 'pear': 4}
"""

cs41 = ["TA_sam", "TA_guido", "student_poohbear", "student_htiek"]
basket = ['apple', 'orange', 'pear']

# Comprehensions
[(x*2)+1 for x in range(4)]
[x % 3 == 0 for x in [3, 5, 9, 8]]
[x[3:] for x in cs41 if x.startswith("TA_")]
[x[0].upper() for x in basket]
[x for x in basket if len(x) < 6]
[(x, len(x)) for x in basket]
{x : len(x) for x in basket}
