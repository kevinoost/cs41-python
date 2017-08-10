#!/usr/bin/env python3 -tt

import re
import collections
from collections import Counter
from collections import namedtuple
#==================== Regular Expressions ====================

m = re.search(r"(\w+) (\w+)", "Isaac Newton, physicist")
assert(m.group(0) == "Isaac Newton")
assert(m.group(1) == "Isaac")
assert(m.group(2) == "Newton")

m = re.match(r"(?P<fname>\w+) (?P<lname>\w+)", "Malcolm Reynolds")
assert(m.group('fname') == 'Malcolm')
assert(m.group('lname') == 'Reynolds')

result = re.sub(r"@\w+\.com", r"@stanford.edu", "sam@msft.com jeff@msft.com")
assert(result == "sam@stanford.edu jeff@stanford.edu")

pattern = re.compile(r'[a-z]+[0-9]{3}')
match = re.search(pattern, '@@@abc123')
assert(match.span() == (3, 9))

"""
Write a regular expression to capture a phone number like
(650) 815-5309
Hint: \d captures [0-9]
"""
def is_phone(number):
    p = re.compile(r"\(\d{3}\) \d{3}-\d{4}")
    return p.match(number) != None

def get_area_code(number):
    p = re.compile(r"\((?P<areacode>\d{3})\) \d{3}-\d{4}")
    m = p.match(number)
    if m:
        return m.group('areacode')

assert(is_phone('(650) 815-5309'))
assert(is_phone('(650) 815-5309, braj'))
assert(not is_phone('+1 (650) 815-5309'))
assert(not is_phone('867.530.9999'))
assert(get_area_code('(650) 815-5309') == '650')

#==================== Collections ====================
"""
defaultdict first example:
    (d.items()) yields:
[('yellow', [1, 3]), ('blue', [2, 4]), ('red', [1])]
"""
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = collections.defaultdict(lambda: list())
for k, v in s:
    d[k].append(v)

"""
defaultdict second example:
    (d.items()) yields:
[('m', 1), ('i', 4), ('s', 4), ('p', 2)]
"""
s = 'mississippi'
d = collections.defaultdict(lambda: 0)
for letter in s:
    d[letter] += 1

#Counter first example:
s = 'mississippi'
count = collections.Counter(s)
print(list(count.items()))
#yields [('s', 4), ('m', 1), ('i', 4), ('p', 2)]

#Counter second example:
cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue']:
    cnt[word] += 1
print(cnt)
#yields Counter({'blue': 2, 'red': 2, 'green': 1})

with open('hamlet.txt', 'r') as f:
    words = re.findall(r'\w+', f.read().lower())
Counter(words).most_common(5)
#yields: [('the', 930), ('and', 843), ('to', 652), ('of', 562), ('i', 517)]

#namedtuple first example:
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
# the usual tuple operations
p[0] + p[1]
x, y = p
x, y
# namedtuple lets you access fields by name:
p.x + p.y
# the following yields Point(x=11, y=22)
p

EmployeeRecord = namedtuple('EmployeeRecord',
                            ['name', 'age', 'title',
                             'department', 'paygrade'])

==================== pathlib ====================
p = pathlib.Path('etc/')
q = p / 'ssh'
print(q) # => etc/ssh
q.exists() # => False
q.is_dir() # => False

p = pathlib.Path.cwd()
print(p) # => [...]/cs41/lab6/lecture-exercises
for f in p.glob('**/*.py'):
    print(f)
#[...]/cs41/lab6/lecture-exercises/in-class-exercises.py

==================== Process Control ====================
import subprocess
import shlex

subprocess.call(["ls", "-l"])
"""
total 312
-rw-r--r--  1 [whoami]  access_bpf  152793 Apr 21 18:08 hamlet.txt
-rw-r--r--  1 [whoami]  access_bpf    3149 Apr 22 10:18 in-class-exercises.py
0
"""
command = "echo 'Hello world' > helloworld.txt"
args = shlex.split(command) # args = ["echo", ... ]
subprocess.call(args)
# Note: this echoed "Hello world > hellowworld.txt" which is not
# what I wanted to happen.

sp_ps = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)
sp_grep = subprocess.Popen(["grep", "Spotify"], stdin=sp_ps.stdout)

==================== pprint ====================
import pprint
ugly = {
    'data': {
        'after': 't3_3q8aog',
        'before': None,
        'kind': 'pagination',
        'children': [{}, {}, {}, {}],
        'uuid': '40b6f818'
    }
}
ugly['recursive'] = ugly
print(ugly)
"""
{'data': {'after': 't3_3q8aog', 'before': None, 'kind': 'pagination', 'children': [{}, {}, {}, {}], 'uuid': '40b6f818'}, 'recursive': {...}}
"""
pprint.pprint(ugly, width=56, depth=2)
"""
{'data': {'after': 't3_3q8aog',
          'before': None,
          'children': [...],
          'kind': 'pagination',
          'uuid': '40b6f818'},
 'recursive': <Recursion on dict with id=4395944696>}
"""

==================== Timing ====================
import timeit
timeit.timeit('"-".join(str(n) for n in range(100))', number = 10000)
# => 0.3080670649651438
timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
# => 0.2591642040060833
timeit.timeit('"-".join(map(str, range(100)))', number=10000)
# => 0.20296815293841064

==================== ** Future ** ====================

from __future__ import print_function
from __future__ import division

==================== Statistics ====================
import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(data)
# => 1.6071428571428572
statistics.median(data)
# => 1.25
statistics.variance(data)
# => 1.3720238095238095

==================== Unicode ====================
import unicodedata
unicodedata.lookup('SLICE OF PIZZA')
# => '🍕'
unicodedata.name('🍕')
# => 'SLICE OF PIZZA'

==================== One-Liners ====================
# Note: I knew most of these already
any([False, True, False]) # => True
all([True, True, False]) # => False

int('45')       # => 45
int('0x2a', 16) # => 42
int('1011', 2)  # => 11
hex(42)         # => '0x2a'
bin(42)         # => '0b101010'

ord('a')        # => 97
chr(97)         # => 'a'

round(123.45, 1)  # => 123.5
round(123.45, -2) # => 100.0

quotient, remainder = divmod(10, 6)
# => quotient, remainder => (1, 4)
max(2, 3) # => 3
max([0, 4, 1]) # => 4
min(['apple', 'banana', 'pear']) # => 'apple'

pow(3, 5)      # => 243
pow(3, 5, 10)  # => 3 (it is (3 ** 5) % 10)

sum([3, 5, 7]) # => 15
sum([[3, 5], [1, 7], [4]], []) # => [3, 5, 1, 7, 4]

