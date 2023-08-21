"""
21.02.2023
Created by: Jessica Göckler
Functions multiple returns
- In exercise 41 you created four differnt functions, now combine them into
  a new function that returns all four results at once
  - return result1,result2,result3,result4
- Call this function at least three times with different parameters and print
  out the results
  - You need three lines that look like this:
    result1,result2,result3,result4 = math_operations(20,5)
  - Choose the numbers you hand over as arguments freely
- Call the function at least once by specifying only 1 variable
  name -> results = math_operations(20,5)
"""
# Addition
def math_operations(a,b):
    addition = a + b
    substraction = a - b
    multiplication = a * b
    division = a / b
    return addition, substraction, multiplication, division

res1, res2, res3, res4 = math_operations(20,5)
res5, res6, res7, res8 = math_operations(8,2)
res9, res10, res11, res12 = math_operations(15,5)
calculations = math_operations(20,28)

print(res1, res2, res3, res4)
print()
print(res5, res6, res7, res8)
print()
print(res9, res10, res11, res12)
print()
print(calculations)


# # Callbacks
# addition1 = sum1(7,5)
# addition2 = sum1(14,12)
# addition3 = sum1(3,6)
# substract1 = subst1(4,3)
# substract2 = subst1(2,3)
# substract3 = subst1(12,50)
# multiply1 = multi_1(7,38)
# multiply2 = multi_1(44,43)
# multiply3 = multi_1(10,30)
# division1 = divi1(14,7)
# division2 = divi1(42,7)
# division3 = divi1(10,5)
# # Printing the results
# print(f"The results of the additions are {addition1}, {addition2} and {addition3}")
# print(f"The results of the substractions are {substract1}, {substract2} and {substract3}")
# print(f"The results of the multiplications are {multiply1}, {multiply2} and {multiply3}")
# print(f"The results of the divisions are {division1}, {division2} and {division3}")
