#!/usr/bin/env python3 -tt

def reassign(arr):
    arr = [4, 1]
    print("Inside reassign: arr = {}".format(arr))

def append_one(arr):
    arr.append(1) 
    print("Inside append_one: arr = {}".format(arr))

l = [4]
print("Before reassign: arr={}".format(l))
# p: Before reassign: arr=[4]
reassign(l)
print("After reassign: arr={}".format(l))
# p.1: Inside reassign: arr = [4, 1]
# p.2: After reassign: arr=[4]

l = [4]
print("Before append_one: arr={}".format(l))
# p: Before reassign: arr=[4]
append_one(l)
print("After append_one: arr={}".format(l))
# p.1: Inside append_one: arr = [4, 1]
# p.2: After reassign: arr=[4, 1]

# Result: Predictions were all correct.
