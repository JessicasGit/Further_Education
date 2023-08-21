"""
14.02.2023
Slicing with a :
- Generate a list with the help of the range functions
- Define 4 different numbers that can be used for slicing the list
- The first number should be an endpoint of a new list,
  the second number a starting point and
  the other two numbers should represent skips you can do with Slicing
- Print out the sliced lists
"""
list1 = list(range(0,20))
print(list1)
print(len(list1))
number1 = 2
number2 = 8
number3 = 3
number4 = 4

print(list1[-number2:-number1])
print(list1[::number3])
print(list1[::number4])
print(list1[:5])
print(list1[5:])
print(list1[::7])
print(list1[::-3])
