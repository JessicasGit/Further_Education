"""
15.02.2023
Removing entries
- Write a program that generates at least three different lists
- print these lists fourth
- Ask the user for one entry from each list he wants to have removed
- let the program remove the entry
- print out the new lists
"""
list1 = list(range(1,10))
print(list1)
rm1 = int(input("Which number do you want to remove? "))
list1.remove(rm1)
print(list1)
rm2 = int(input("Which number do you want to remove also? "))
list1.remove(list1[rm2])
print(list1)
print()

list2 = list(range(5,40,2))
print(list2)
rm3 = int(input("Which number do you want to remove? "))
list2.remove(rm3)
print(list2)
rm4 = int(input("Which number do you want to remove also? "))
list2.remove(list2[rm4])
print(list2)
print()

list3 = ["January", "February", "March", "April", "May", "June", "July"]
print(list3)
rm5 = input("Which month do you want to remove? ")
list3.remove(rm5)
print(list3)
rm6 = (input("Which month do you want to remove also? "))
list3.remove(rm6)
print(list3)
