"""
22.02.2023
Created by: Jessica Göckler
Reading a file
- Read on your second file from exercise 59, the one with the countdown,
  by using the generator method
  - You need to write a loop after your with statement to be able to read in
    line by line
- Calculate the sum of the numbers and print out the result
  - Don't forget that everything we read in is a string so you need to cast
    the lines to int() before you can sum them up
"""
sum1 = 0 # Defines the value of the variable sum1
with open("Exercise_59_2.txt","r") as read_file1: # opens the named file and reads in as read_file1
        for line in read_file1:
             sum1 += int(line) # sums the value of the lines
             # print(line)
             # print(repr(line))
             # print(line.strip('\n'))
print()
print("The sum of all numbers in the file is: ",sum1)
