#!/usr/bin/env python3 -tt

def say_hello():
    print("Hello!")

print(say_hello())
# Prediction:
# Hello!
# None
# Result: Correct!

def echo(arg=None):
    print("arg:", arg)
    return arg

print(echo())
# Prediction:
# arg: None
# None
# Result: Correct!

print(echo(5))
# Prediction:
# arg: 5
# 5
# Result: Correct!

print(echo("Hello"))
# Prediction:
# arg: Hello
# Hello
# Result: Correct!

def drive(has_car):
    if not has_car:
        return
    return 100

drive(False)
# Prediction: (no output, interpreter does not print None)
# Result: Correct!
drive(True)   # => ?
# Prediction: 100
# Result: Correct!
