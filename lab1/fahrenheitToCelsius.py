#!/usr/bin/env python3
"""
File: fahrenheitToCelsius.py
"""
fahrenheitTemp = float(input("Temperature F? "))
celsiusTemp = (fahrenheitTemp - 32.0) * 5/9
celsiusTemp = round(celsiusTemp, 2)
print("It is {} degrees Celsius.".format(celsiusTemp))
