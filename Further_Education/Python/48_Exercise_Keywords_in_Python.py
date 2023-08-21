"""
22.02.2023
Created by: Jessica Göckler
Keywords in Python
- Create a list with at least 15 entries you choose
- Iterate over it with a for loop and add up the elements
- Create one if statement in your loop that can't be true and add pass
- Include a second if statement in your loop that breaks the loop if your sum
  gets bigger than a threshold (you choose)
- Include a third if statement in your loop that uses continue if the current
  entry of your list is in a specific range, e.g. 50 to 60, and prints out
  something in all other cases (use else)
- Print out the sum at the end.
"""
list1 = [2, 7, 10, 11, 12, 15, 18, 19, 29, 30, 32, 36, 42, 46, 48]
sum1 = 0
"""
for i in list1:
    sum1 = sum1 + i
    print(i)
    print()
    if i < 0:
        pass
    if sum1 > 50:
        break
    if i == range(50,60):
        continue
    print("End of Loop")
"""
for i in range(20):
    sum1 = sum1 + i
    print(i)
    print()
    if i < 0:
        pass
    if sum1 > 50:
        break
    if i == range(50,60):
        continue
    print("End of Loop")
