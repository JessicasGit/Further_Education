"""
17.02.2023
For Loops
Created by: Jessica Göckler
- All following loops should run at least over a range from 0 to 21
- Write one loop that sums up all numbers in the set range
- Write another loop that sums up only the even numbers in the set range
- Write a third loop that generates a list that contains the values
  of the range in reverse order
- Print out all three results
"""
sum1 = 0
for i in range(0,22,2):
    sum1 += i
print("Sum of all numbers: \n",sum1)
print()

sum_even = 0
list1 = list(range(0,22,2))
# define i as 0 and increase its value by 2 after each iteration until you reach 21
for i in list1:
#    print(list1)
    sum_even += i
print("Sum of the even numbers: \n",sum_even)
print()

rev_list = []
# for i in range(21,-1,-1):    This is not ideal!
#     rev_list.append(i)
# Better and much easier :
for i in range(22):
    rev_list.append(21-i)
#    print(i)
print("Reverse order of the range: \n",rev_list)

# sum2 = 0
# list1 = list(range(0,20,4))
# for i in list1:
#     print(sum2)
#     print(i)
#     print(list1)
#     sum2 += i
#
# print(sum2)
# print(list1)
