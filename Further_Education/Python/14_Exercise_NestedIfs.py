"""
13.02.2023
- Rework your program from Exercise 13 with the use of nested if statements
  instead of the lobical operators
  - and
  - or
"""
number1 = int(input("Number 1 of 4: "))
number2 = int(input("Number 2 of 4: "))
number3 = int(input("Number 3 of 4: "))
number4 = int(input("Number 4 of 4: "))

if number1 == number2 and number3 == number4:
    print("Nr 1 and 2 are as eqaul to eachother as Nr 3 and 4")
    if number1 == number3 and number2 == number4:
        print("Nr 1 and 3 are as eqaul to eachother as Nr 2 and 4")
    else:
        print("This equal comparison is not working.")
else:
    print("Try again to get equal Nrs.")
if number1 == number4 or number2 == number3:
    print("Nr 1 and 4 or Nr 2 or 3 are eqaul to eachother")
    if number1 > number2 and number3 > number4:
        print("Nr 1 is greater than Nr 2 and Nr 3 is greater than Nr 4.")
    else:
        print("This equal and greater than comparison is not working.")
else:
    print("Try again to get an equal and greater than comparison.")

if number1 < number3 and number2 < number4:
    print("Nr 1 is smaller than Nr 3 and Nr 2 is smaller than Nr 4.")
    if number1 <= number4 and number2 == number3:
        print("Nr 1 is equal or smaller than Nr 4 and Nr 2 equals Nr 3")
    else:
            print("This comparison is not working. ")
else:
        print("Try again.")
if number1 > number4 or number2 >= number3:
    print("Nr 1 is greater than Nr 4 or Nr 2 is greater than or equals Nr 3")
else:
    print("Try again.")
