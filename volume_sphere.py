'''
        Program: volume_sphere.py
        Written by: Elayna Ridley
        Purpose: Calculate the volume of a sphere given it's diameter.
        How to use: Run this from the command line and enter the diameter when asked. Enter a real number.
        Input: The diameter of a sphere.
        Output: The volume of a sphere.
'''

import math

diam = float(input('Enter a real number that is the diameter: '))

r = diam/2

vol = (4 * math.pi * r ** 3)/3

answer = vol

print ("The volume is",("%.2f" % answer), 'cubic inches')
