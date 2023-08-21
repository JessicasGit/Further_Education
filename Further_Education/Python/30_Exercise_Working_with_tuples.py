"""
16.02.2023
Created by: Jessica Göckler
- Write a program that creates 4 touples for different lengths
- The lengths should be dictated by the user
- Print out the touples
- Afterwards let the user choose one entry from each tuple to be displayed
- Try to generate a tuple with duplicate values
"""
input_number1 = int(input("How long ist your first tuple? "))
input_number2 = int(input("How long ist your second tuple? "))
input_number3 = int(input("How long ist your third tuple? "))
input_number4 = int(input("How long ist your fourth tuple? "))

tuple1 = tuple(range(input_number1))
tuple2 = tuple(range(input_number2))
tuple3 = tuple(range(input_number3))
tuple4 = tuple(range(input_number4))
tuple5 = (1,2,3,4,3,4,5,5,6)

print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)

input_index1 = int(input("Which index of thr first tuple do you want to see? "))
input_index2 = int(input("Which index of thr second tuple  do you want to see? "))
input_index3 = int(input("Which index of thr third tuple  do you want to see? "))
input_index4 = int(input("Which index of thr fourth tuple  do you want to see? "))

print(tuple1[input_index1])
print(tuple2[input_index2])
print(tuple3[input_index3])
print(tuple4[input_index4])

print(tuple5)
