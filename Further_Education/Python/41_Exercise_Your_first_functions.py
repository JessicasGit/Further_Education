"""
21.02.2023
Created by: Jessica Göckler
Functions
- Create a program that defines functions for the four mathematical basic
  operations(+, -, *, /)
  - One function for one operation, e.g. sum_up for addition
  - Each function should take two parameters/arguments and return
    the result of the calculation
- Call each of the functions at least three times with different parameters
  - That means you need 12 different statements tat look like this:
    result1 = sum_up(12,8) for example
  - You can choose whatever numbers you want to hand over you functions as
    arguments.
"""
# Addition
def sum1(a,b):
    result = a+b
    return result
# Substraction
def subst1(a,b):
    result = a-b
    return result
# Multiplication
def multi_1(a,b):
    result = a*b
    return result
# Division
def divi1(a,b):
    result = a/b
    return result
# Callbacks
addition1 = sum1(7,5)
addition2 = sum1(14,12)
addition3 = sum1(3,6)
substract1 = subst1(4,3)
substract2 = subst1(2,3)
substract3 = subst1(12,50)
multiply1 = multi_1(7,38)
multiply2 = multi_1(44,43)
multiply3 = multi_1(10,30)
division1 = divi1(14,7)
division2 = divi1(42,7)
division3 = divi1(10,5)
# Printing the results
print(f"The results of the additions are {addition1}, {addition2} and {addition3}")
print(f"The results of the substractions are {substract1}, {substract2} and {substract3}")
print(f"The results of the multiplications are {multiply1}, {multiply2} and {multiply3}")
print(f"The results of the divisions are {division1}, {division2} and {division3}")
