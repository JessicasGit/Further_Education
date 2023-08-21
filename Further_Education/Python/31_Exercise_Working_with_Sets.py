"""
17.02.2023
Working with Sets
Created by: Jessica Göckler
- Write a program that creates 4 sets of different lengths
- The lengths should be dictated by the user
- Print out the sets
"""
input1 = int(input("Please specify the range of your first set: "))+1
set1 = set(range(input1))
print(set1)

input2 = int(input("Please specify the range of your second set: "))+1
set2 = set(range(input2))
print(set2)

input3 = int(input("Please specify the range of your third set: "))+1
set3 = set(range(input3))
print(set3)

input4 = int(input("Please specify the range of your fourth set: "))+1
set4 = set(range(input4))
print(set4)

set5 = {5,6,7,8,5,1,2,5,4,6}
print(type(set5))
print(set5)


#list1 = list(set(list1))
