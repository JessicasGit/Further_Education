"""
21.02.2023
Created by: Jessica Göckler
Functions with loops
- Write a program that contains two different functions which both take a list
  as argument
- The first function returns the sum of all elements in the list,
  calculated by a loop
  - You can use the loop you defined on your previous exercises and put it into
    your function via copy and paste, but don't forget to adjust the intendation
- The second function searches for the biggest element inside the handed over
  list by using a loop containing an if statement, similar to an
  earlier exercise.
"""
def addition(inputlist):
    result = 0
    for elem in inputlist:
        result += elem
    return result

def max_number(inputlist):
    result = 0
    for elem in inputlist:
        if elem > result:
            result = elem
    return result

list1 = list(range(22))
list2 = list(range(18))

sum1 = addition(list1)
sum2 = addition(list2)

max1 = max_number(list1)
max2 = max_number(list2)

print(sum1)
print(sum2)
print(max1)
print(max2)
