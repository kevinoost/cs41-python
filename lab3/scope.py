#!/usr/bin/env python3 -tt

# Case 1
x = 10

def foo():
    print("(inside foo) x:", x)
    y = 5
    print('value:', x * y)

print("(outside foo) x:", x)
foo()
print("(after foo) x:", x)
""" Output:
(outside foo) x: 10
(inside foo) x: 10
value: 50
(after foo) x: 10

As predicted
"""

# Case 2
x = 10

def foo():
    x = 8  # Only added this line - everything else is the same
    print("(inside foo) x:", x)
    y = 5
    print('value:', x * y)

print("(outside foo) x:", x)
foo()
print("(after foo) x:", x)
""" Output:
(outside foo) x: 10
(inside foo) x: 8
value: 40
(after foo) x: 10

As predicted
"""

# Case 3
x = 10

def foo():
    print("(inside foo) x:", x)  # We swapped this line
    x = 8                        # with this one
    y = 5
    print('value:', x * y)

print("(outside foo) x:", x)
foo()
print("(after foo) x:", x)
# (outside foo) x: 10
# UnboundLocalError: local variable 'x' referenced before assignment
# (after foo) x: 10
#
# Here x is defined in the function, so the earlier reference to x
# in that function is intended by the interpreter to be the same x
# that is defined later in the function, so we cause an
# UnboundLocalError.

lst = [1,2,3]
def foo():
    lst.append(4)
foo()
# lst = [1,2,3,4] now, as predicted

lst = [1,2,3]
def foo():
    lst = lst + [4]
foo()
# Again, an UnboundLocalError because by assigning lst the value
# of "lst + [4]" the scope of lst become the function foo, and
# when the right-hand side (lst + [4]) is evaluated, we see that
# it references a variable (namely, lst) that is at that point
# unbound.

x = 5

def square(num=x):
    return num * num

x = 6
f()   # => 25, not 36
f(x)  # => 36

def append_twice(a, lst=[]):
    lst.append(a)
    lst.append(a)
    return lst
def append_twice(a, lst=[]):
    lst.append(a)
    lst.append(a)
    return lst
   
# Works well when the keyword is provided
append_twice(1, lst=[4])  # => [4, 1, 1]
append_twice(11, lst=[2, 3, 5, 7])  # => [2, 3, 5, 7, 11, 11]

# But what happens here?
print(append_twice(1))
print(append_twice(2))
print(append_twice(3))

"""Output:
[1, 1]
[1, 1, 2, 2]
[1, 1, 2, 2, 3, 3]
As predicted. lst is bound to a particular default empty list
at the point of function definition, not to a new default list
every time that the function is called.
"""

def all_together(x, y, z=1, w=2, *nums, indent=True, spaces=4, **options):
    print("x:", x)
    print("y:", y)
    print("z:", z)
    print("w:", w)
    print("nums:", nums)
    print("indent:", indent)
    print("spaces:", spaces)
    print("options:", options)

