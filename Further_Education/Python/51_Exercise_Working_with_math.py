"""
23.02.2023
Created by: Jessica Göckler
Working with math
- Write a program that defines two numbers (x and y) and caldulates new values
  with the help of the math functions on the previous slides (exp, log, log2,
  log10, pow, sqrt, cos, sin, tan, acos, asin, atan)
- You can define the numbers simply on your own by using x = 5 and y = 10
  for example
- Print out the results
"""
import math

x = 1
y = 10
z = 5

res1 = math.exp(z)
res2 = math.log(z)
res3 = math.log2(y)
res4 = math.log10(z)
res5 = math.pow(y,z)
res6 = math.sqrt(z)
res7 = math.cos(y)
res8 = math.sin(z)
res9 = math.tan(y)
res10 = math.acos(x) # only defined for inputs between -1.0 and 1.0 there's no possible (real) angle whose cosine is greater than 1
res11 = math.asin(x) # only defined for inputs between -1.0 and 1.0 there's no possible (real) angle whose sine is greater than 1
res12 = math.atan(-1)
res13 = math.isnan(y)


print(res1,"\n")
print(res2,"\n")
print(res3,"\n")
print(res4,"\n")
print(res5,"\n")
print(res6,"\n")
print(res7,"\n")
print(res8,"\n")
print(res9,"\n")
print(res10,"\n")
print(res11,"\n")
print(res12,"\n")
print(res13,"\n")
