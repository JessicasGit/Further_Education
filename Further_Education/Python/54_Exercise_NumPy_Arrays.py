"""
23.02.2023
Created by: Jessica Göckler
NumPy Arrays
- Write a simple python program that generates the following arrays:
  - An array consisting of 25 zeros
  - An array consisting of 8 ones
  - An array consisting of numbers from 0 to 24 in order
  - An array consisting of 9 entries of your choice
  - An two-dimensional array TD consisting of 6 rows of arrays with 5 entries each
  - A transposed version of the two-dimensional array TD
- Write furthermore an algorithm to print out the sum, maximum value,
  minimum value and shape of all created Arrays
"""
import numpy as np

array1 = np.zeros(25)
array2 = np.ones(8)
array3 = np.arange(25)
array4 = np.array([3,4,9,9,11,12,15,16,20])
array5 = np.random.randn(6,5)
print(array5.transpose())
print()
print(array1,"\n",array1.sum(),"\n",array1.min(),"\n",array1.sum(),"\n",array1.shape,"\n")
print(array2,"\n",array2.sum(),"\n",array2.min(),"\n",array2.sum(),"\n",array2.shape,"\n")
print(array3,"\n",array3.sum(),"\n",array3.min(),"\n",array3.sum(),"\n",array3.shape,"\n")
print(array4,"\n",array4.sum(),"\n",array4.min(),"\n",array4.sum(),"\n",array4.shape,"\n")
print(array5,"\n",array5.sum(),"\n",array5.min(),"\n",array5.sum(),"\n",array5.shape,"\n")
