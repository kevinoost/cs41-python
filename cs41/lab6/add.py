#!/usr/bin/env python3 -tt

import sys
import re

def is_number(arg):
    try:
        float(arg)
        return True
    except ValueError:
        return False

if len(sys.argv) == 1:
    print("Usage: python3 add.py <nums>\n\n	Add some numbers together")
else:
    numbers = map(float, filter(is_number, sys.argv[1:]))
    print(sum(numbers))
