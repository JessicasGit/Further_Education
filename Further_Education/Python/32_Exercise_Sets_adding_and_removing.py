"""
17.02.2023
Adding and removing
Created by: Jessica Göckler
- Take your sets from exercice 31
- Remove some elements from them
- Try to remove two elements directly one after other
- Check whick elements were removed with the print command
- Add the elements again to the set
- Print out the new sets
- What changes can you see?
"""
input1 = int(input("Please specify the range of your first set: "))+1
input2 = int(input("Please specify the range of your second set: "))+1
input3 = int(input("Please specify the range of your third set: "))+1
input4 = int(input("Please specify the range of your fourth set: "))+1

set1 = set(range(input1))
set2 = set(range(input2))
set3 = set(range(input3))
set4 = set(range(input4))

print(set1)
print(set2)
print(set2)
print(set3)
print(set4)
print()
set1.remove(3)
print(set1)
elem1 = set1.pop()
elem2 = set1.pop()
print(set1)
set1.add(elem1)
set1.add(elem2)
print(set1)

# set2.remove()
# elem3 = set2.pop()
# print(set2)
# elem4 = set2.pop()
# print(set2)
# set2.add(elem3)
# print(set2)
# set2.add(elem4)
#
# set3.remove()
# elem5 = set3.pop()
# print(set3)
# elem6 = set3.pop()
# print(set3)
# set3.add(elem5)
# print(set3)
# set3.add(elem6)
#
# set4.remove()
# elem7 = set4.pop()
# print(set4)
# elem8 = set4.pop()
# print(set4)
# set4.add(elem7)
# print(set4)
# set4.add(elem8)
