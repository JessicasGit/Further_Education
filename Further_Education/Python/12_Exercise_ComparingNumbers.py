"""
13.02.2023
- Write a program that defines 4 numbers
- The program should pront out a positive encouragement if one of these
  conditions are fulfilled and a negative encouragement if none of them are true
  - Number1 = Number2 and Number3 = Number4
  - Number1 = Number3 and Number2 = Number4
  - Number1 = Number4 or Number2 = Number3
"""
number1 = int(input("Number 1 of 4: "))
number2 = int(input("Number 2 of 4: "))
number3 = int(input("Number 3 of 4: "))
number4 = int(input("Number 4 of 4: "))

if number1 == number2 and number3 == number4:
    print("Pair 1 and 2 are also equal as pair 3 and 4.")
elif number1 == number3 and number2 == number4:
    print("Pair 1 and 3 are also equal as pair 2 and 4.")
elif number1 == number4 or number2 == number3:
    print("Pair 1 and 4 or are equal 2 and 4 to eachother.")
else:
    print("These pairs are not equal to eachother.")

"""
Alternative:

if number1 == number2 and number3 == number4:
    print("Pair 1 and 2 are also equal as pair 3 and 4.")
else:
    print("These pairs are not equal to eachother.")

if number1 == number3 and number2 == number4:
    print("Pair 1 and 3 are also equal as pair 2 and 4.")
else:
    print("These pairs are not equal to eachother.")

if number1 == number4 or number2 == number3:
    print("Pair 1 and 4 or are equal 2 and 4 to eachother.")
else:
    print("These pairs are not equal to eachother.")
"""
