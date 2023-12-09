#!/usr/bin/python3

import math

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b **2)

if __name__== "__main__":
    a = int(input("Enter the length: "))
    b = int(input("Enter the width: "))
    c = int(calculate_hypotenuse(a, b))
    print(c)