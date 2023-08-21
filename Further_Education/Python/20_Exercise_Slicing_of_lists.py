"""
14.02.2023
Slicing of lists
- Create 2 different lists with contents of your choice
- define four numbers
- use them to slice your lists
- What happens if you use numbers that are bigger than the size of you lists?
"""
list1 = list(range(0,20))
print(list1)
print(len(list1))
print(list1[2:8])
print(list1[11:50])
print()

list2 = list(range(5,30))
print(len(list2))
print(list2)
number1 = 2
number2 = 10
print()

print(list2[0:3])
print(list2[11:50])
print(list2[number1:number2])
