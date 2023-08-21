"""
22.02.2023
Created by: Jessica Göckler
New modules
- Write a program that asks the user so guess a specific number
- Generate a random number between 0 and 99, search the library to find
  a module and a function for this task
- Generate a while loop that asks for a guess as long as the user didn't guess
  right
   - This is where you have to define your input
- Print out hints if the user is lower or higher than the random number by
  using an if/elif/else statement
- Count the number of guesses the user needed and print them out after the user
  guessed correctly
"""
import random
ran1 = random.randint(0 ,99)
# print(ran1)

print("Guess a random number between 0 and 99!")
input1 = int(input("Now guess your number: "))
count = 0

while input1 != ran1:
    if input1 > ran1:
        print("The number you guessed is bigger than the generated number!")
    elif input1 < ran1:
        print("The number you guessed is smaller than the generated number!")
    input1 = int(input("Try it again! "))
    count += 1

print(f"You guessed the right number and tied it {count-1} times")
