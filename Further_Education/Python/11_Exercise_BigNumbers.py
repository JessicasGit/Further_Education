"""
13.02.2023
Define 2 numbers
"""
number1 = int(input("Type in number1: "))
number2 = int(input("Type in number2: "))
sum = number1 + number2

# doing this instead of sum is also possible, but when the program is longer,
# it is better to do the math beforehand

if (number1 + number2) > 100:
    print("That is a big number.")
elif sum > 10:
    print("That is a mediocre number.")
elif sum > 5:
    print("That is a small number.")
else:
    print("This is a very small number.")
