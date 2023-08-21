"""
14.02.2023
The last values
- Use your lists from ex 18 and 17 an print out the last element,
  as well as the third to last and fifth to last element of using negative
  indices
"""
list1 = list(range(50,0,-2)) # skipping 2
print(list1)
print(len(list1))
print(list1[-3],list1[-1])
print()

list2 = list(range(0,44,4)) # skipping 4
print(list2)
print(len(list2))
print(list2[0])
print(list2[3])
print()

list3 = list(range(4,35))
print(list3)
print(len(list3))
print(list3[-1])
print(list3[-5])
print()

list4 = list(range(5,20))
print(list4)
print(len(list4))
print(list4[-5],list4[-1])
print(list4[2:8])
print()
