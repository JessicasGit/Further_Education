"""
20.02.2023
Loop through a matrix
Created by: Jessica Göckler
- Write a program that uses nested loops to tackle the tasks below:
  - Search for the biggest number of the matrix, by including an if-clause
    inside your loops and saving the corresponding value in a variable you
    overwrite everytime your of becomes True
  - Sum up all numbers in the matrix so that you have one number at the end
  - Describe the multiplication of the components of two matrices in a third
    resulting matrix, which contains only zeros at the start of your loops
  - The outer loop always runs through the outer list (sublist by sublist)
    an the inner loop runs through the elements of the sublists.
"""
matrix1 = [[10,12,13], [17,18,19], [14,15,16]]
matrix2 = [[1,2,3], [7,8,9], [4,5,6]]
matrix3 = [[0,0,0], [0,0,0], [0,0,0]]

maximum_number = 0
for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        if maximum_number < matrix1[i][j]:
            maximum_number = matrix1[i][j]
        #     print("Maximum number",maximum_number)
        # else:
        #     print("No maximum number found")
print("Maximum number found",maximum_number)
print()

sum1 = 0
for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        sum1 = sum1 + matrix1[i][j]
print(sum1)
print()

for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        matrix3[i][j] = matrix1[i][j] * matrix2[i][j]
print(matrix3)
