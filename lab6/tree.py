#!/usr/bin/env python3 -tt

import sys
import pathlib

p = pathlib.Path.cwd()
if len(sys.argv) > 1:
    directory = sys.argv[1]
    p = pathlib.Path(sys.argv[1])

print(p)
