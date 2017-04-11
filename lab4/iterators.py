#!/usr/bin/env python3 -tt

it = iter(range(100))
67 in it  # => True

next(it)  # => 68
37 in it  # => False (!)
# This is because the iterator has advanced
# past 37, and there is no other 37 in the
# remainder of the stream.
next(it)
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

This is because the remainder of the stream
was consumed unsuccessfully searching for
the value 37.
"""
