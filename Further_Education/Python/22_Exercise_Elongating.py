"""
14.02.2023
Longer lists
- Write a program that generates 6 different lists
- Append the third list to first one and
  the fourth list to the second one. e.g. list1.append(list3)
- Extend the first list with the help of the fifth list and
  the second one with the help of the sixth list, e.g. list1.extend(list5)
"""
list1 = list(range(0,20))
print(list1)
#print(len(list1))
print()
list2 = list(range(4,16,4))
print(list2)
#print(len(list2))
print()
list3 = list(range(5,20))
print(list3)
#print(len(list3))
print()
list4 = [7, 13 , 42, 87]
print(list4)
#print(len(list4))
print()
list5 = [1.2, 3.4, 5.6, 7.8]
print(list5)
#print(len(list5))
print()
list6 = list(range(0,15,2))
print(list6)
#print(len(list6))
print()
list1.append(list3)
print(list1)
list2.append(list4)
print(list4)
list1.extend(list5)
print(list1)
list2.extend(list6)
print(list2)
