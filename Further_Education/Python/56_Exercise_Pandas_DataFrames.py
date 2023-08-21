"""
23.02.2023
Created by: Jessica Göckler
Pandas DataFrames
- Write a program that creates a DataFrame consisting of at least 4 rows and
  6 columns
- It should contain random numbers generated via NumPy
- Create 6 new DataFrames by sorting the original DataFrame alongside the
  columns (df. sort_values())
- Let the program print a description of the original DataFrame
  - What do these numbers mean?
"""
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(np.random.randn(4,6), index=["Row1","Row2","Row3","Row4"], columns=["ColA","ColB","ColC","ColD","ColE","ColF"])

print(dataframe.sort_values(by="ColA"),"\n")
print(dataframe.sort_values(by="ColB"),"\n")
print(dataframe.sort_values(by="ColC"),"\n")
print(dataframe.sort_values(by="ColD"),"\n")
print(dataframe.sort_values(by="ColE"),"\n")
print(dataframe.sort_values(by="ColF"),"\n")

# print(dataframe.index,"\n")
# print(dataframe.columns,"\n")
#
# print(list(dataframe.index),"\n")
# print(list(dataframe.columns),"\n")

print(dataframe.describe())
