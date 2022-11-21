#!/usr/bin/python3

# program to check if a number is power of 2.

def power_of_two(x):
    return not (x & (x - 1))

        