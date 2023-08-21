"""
10.02.2023
4 different inputs
    2 of these inputs should be numbers
        Print out the handed ofer string variobles
            Let the program do at least two different mathematical operations
            (+ or - or * or /) with the numbers and print out
            the results of these operations
"""

number_input1 = input("Please give me a Number: ")
number_input2 = input("Please give me a further Number: ")
greeting_input1 = input("Type in something: ")
greeting_input2 = input("Type something else: ")

print()
print(int(float(number_input1)))
print(int(float(number_input2)))
print()
print(greeting_input1)
print(greeting_input2)
print(greeting_input1,greeting_input2)
print()
print(f"Adding the two numbers {int(float(number_input1)) + int(float(number_input2))}")
print(int(float(number_input1)) * int(float(number_input2)))
