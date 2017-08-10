#!/usr/bin/env python3
"""
File: fahrenheit-to-celsius.py

Problem: Write a program to convert degrees Fahrenheit to degrees Celcius by (1) asking the user for a number (not necessarily integral) representing the current temperature in degrees Fahrenheit, (2) converting that value into the equivalent degrees Celsius, and (3) printing the final equivalent value.

Challenge: Print the final temperature to two decimal places.
"""

def fahreinheitToCelsius():
    fahrenheitTemp = float(input("Temperature F? "))
    celsiusTemp = (fahrenheitTemp - 32.0) * 5/9
    celsiusTemp = round(celsiusTemp, 2)
    print("It is {} degrees Celsius.".format(celsiusTemp))

if __name__ == '__main__':
    fahreinheitToCelsius()
