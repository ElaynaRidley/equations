'''
        Program: quadratic.py
        Written by: Elayna Ridley
        Purpose: To calculate the value of x.
        How to use: Enter three numbers eperated by a comma when prompted.
        Input: three numbers seperated by a comma.
        Output: The value x
'''

import math

print("Type in A, B, C as the coefficients of the quadratic equation.")
temp = input("Enter three numbers separated by commas: ")
a = float(temp.split(",")[0])
b = float(temp.split(",")[1])
c = float(temp.split(",")[2])

print("a = ",a)
print("b = ",b)
print("c = ",c)

x = (-b + math.sqrt(b ** 2 - 4 * a * c))/(2 * a)
z = (-b - math.sqrt(b ** 2 - 4 * a * c))/(2 * a)

print ("x is",("%.2f" % x), "or", ("%.2f" % z))
