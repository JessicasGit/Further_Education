"""
13.02.2023
- Tatke the program from Ex. 12 and add some more statements for printing out
  a positive encouragement
  - Number1 > Number2 and Number3 > Number4
  - Number1 < Number3 and Number2 < Number4
  - Number1 <= Number4 and Number2 = Number3
  - Number1 > Number4 or Number2 >= Number3
"""
number1 = int(input("Number 1 of 4: "))
number2 = int(input("Number 2 of 4: "))
number3 = int(input("Number 3 of 4: "))
number4 = int(input("Number 4 of 4: "))

if number1 == number2 and number3 == number4:
    print("This comparison is working.")
elif number1 == number3 and number2 == number4:
    print("This comparison is working.")
elif number1 == number4 or number2 == number3:
    print("This comparison is working.")
elif number1 > number2 and number3 > number4:
    print("This comparison is working.")
elif number1 < number3 and number2 < number4:
    print("This comparison is working.")
elif number1 <= number4 and number2 == number3:
    print("This comparison is working.")
elif number1 > number4 or number2 >= number3:
    print("This comparison is working.")
else:
    print("This comparison is not working.")
