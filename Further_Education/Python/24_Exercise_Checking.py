"""
15.02.2023
Checking for values
- Write a program that generates a list with contents of your choice
- Now let the user input at least three different things
- Check wheter these inpts are part of your list or not
- Print out an appropriate answer
"""
list1 = ["February","March","April","May","June","July",
         "August","September","October","November","December"]

Check1 = input("In which month is your birthday? ")
Check2 = input("Which month is your favourite? ")
Check3 = input("Which month are you looking for? ")

if Check1 in list1:
    print("How interesting! ")
print()

if Check2 in list1:
    print("That's nice to know! ")
print()

if Check3 not in list1:
    print("Sorry, I can not find it. ")
