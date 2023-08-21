"""
14.02.2023
Working with the range and len()
- Create 4 lists with different lengths by using the range() functions
- let the program print out the generated lists as well as the corresponding lengths
- Skipping parts with range
"""
# Just to show the steps in detail
# list1 = range(50,0,-2)
# print(list1)
# print(type(list1))
# list1 = list(list1)
# print(list1)
# print(type(list1))
# print(len(list1))

list1 = list(range(50,0,-2)) # skipping 2
print(list1)
print(len(list1))

list2 = list(range(0,44,4)) # skipping 4
print(list2)
print(len(list2))

list3 = list(range(4,34))
print(list3)
print(len(list3))

list4 = list(range(5,20))
print(list4)
print(len(list4))
