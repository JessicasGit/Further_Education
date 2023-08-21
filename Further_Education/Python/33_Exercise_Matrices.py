"""
17.02.2023
Matrices
Created by: Jessica Göckler
- Write a program that creates at least 3 different matrices with
  different sizes
- For this exerceise rows stands for the numbers of sublists
  and colums for the number of entries in the sublists
- One of them should be quadratic
- One should have more columns than rows
- One should have more rows than columns
"""
matrix1 = [list(range(3)), list(range(3)), list(range(3))]
matrix2 = [list(range(5)), list(range(5))]
matrix3 = [list(range(3)), list(range(3)), list(range(3)), list(range(3))]

print(matrix1)
matrix1[1][1] = 20
print(matrix1)
print()
print(matrix2)
matrix2[0][3] = 8
print(matrix2)
print()
print(matrix3)
print()
