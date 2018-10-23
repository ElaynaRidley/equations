'''
        Program: normal.py
        Written by: Elayna Ridley
        Purpose: Calculate the probability density.
        How to use: Enter x, the variance, and the mean in that order seperated by commas.
        Input: Sigma squared, x, and mew.
        Output: The probability density.
'''

import math

print("Type in three values to calculate the normal probability density at x.")
print("   x, variance, mean")
temp = input("Enter these three numbers separated by commas: ")
x = float(temp.split(",")[0])
variance = float(temp.split(",")[1])
mean = float(temp.split(",")[2])

sig = variance

mew = mean

f = (1 * math.e ** -(((x - mew) ** 2)/(2 * sig)))/(math.sqrt(2 * math.pi * sig))

print ("f is ",("%.2f" % f))
