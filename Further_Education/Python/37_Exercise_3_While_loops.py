"""
20.02.2023
3 While Loops
Created by: Jessica Göckler
- Write a program that uses while loops to finish the tasks below,
  unknown length means that you define the length by yourself,
  e.g. with range or by simply creating a list on your own,
  but don't print it out:
  - searching for a specific number (e.g. 5) in an integer list of
    unknown length
  - Multiplying all elements with each other of an integer list of unknown
    length (7 elements at least and 15 at maximum)
  - Printing out the contents of a string list of unknown length elementwise
"""
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
input1 = int(input("Choose a number. \n"))
# fist part
while input1 != 5 in list1:
    print("We try to reach number 5!")
    input1 = int(input("Try again: "))
print("We found",input1,"in the list.")
# second part
i = 0
mult1 = 1
while i < len(list1):
    mult1 = mult1 * list1[i]
    i += 1
    print(mult1)
# second part with range
list2 = list(range(20))
i = 1
mult1 = 1
while i < len(list2):
    mult1 = mult1 * list2[i]
    i += 1
    print(mult1)
# third part
list3 = ["Plastid", "Nucleus", "Mitochondria", "Endoplaspatic reticulum"]
i = 0
while i < len(list3):
    print(list3[i])
    i += 1
