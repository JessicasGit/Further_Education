"""
15.02.2023
Inserting values
- Write a program that generates three lists of different sizes
  and print them out
- Afterwards insert values into these lits at points of your choice
"""
insert1 = "October"
insert2 = 3
insert3 = "Hello"
insert4 = 555

list1 = ["February","March","April","May","June","July",
         "August","September","November","December"]
print(list1)

list1.insert(2,insert4)
print(list1)

list1.insert(-9,insert1)
print(list1)
print()

list2 = list(range(0,20,2))
print(list2)

list2.insert(10,insert3)
print(list2)

list2.insert(-1,insert4)
print(list2)
print()

list3 = list(range(0,60,30))
print(list3)

list3.insert(5,insert1)
print(list3)

list3.insert(-12,insert2)
print(list3)
