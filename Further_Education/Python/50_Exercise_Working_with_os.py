"""
23.02.2023
Created by: Jessica Göckler
Working with os
- Create a directory structure by using os
- Create one partent directory with at least five child directories
- Create a file in each directory simply by using os and by changing
  directories beforehand
  - You need to use os.chdir() to go to the corresponding directory
  - afterwards your need to use os.system("touch....") to create the file
  - Then you need to use again os.chdir() to move back to the parent directory
  - Do this for all five child directories you created before
"""
import os
os.makedirs("OS")
print(os.getcwd())
print()
os.chdir("OS")
print(os.getcwd())
print()
os.makedirs("First")
os.makedirs("Second")
os.makedirs("Third")
os.makedirs("Fourth")
os.makedirs("Fifth")
# move to the First child dir
os.chdir("First")
print(os.getcwd())
print()
# create an empty file
os.system("touch one.txt")
# move back to parent dir
os.chdir("..")
print(os.getcwd())
print()
# move to the Second child dir and create an empty file and move back to parent dir
os.chdir("Second")
print(os.getcwd())
print()
# create an empty file
os.system("touch two.txt")
# move back to parent dir
os.chdir("..")
print(os.getcwd())
print()
# move to the Third child dir and create an empty file and move back to parent dir
os.chdir("Third")
print(os.getcwd())
print()
# create an empty file
os.system("touch three.txt")
# move back to parent dir
os.chdir("..")
print(os.getcwd())
print()
# move to the Fourth child dir and create an empty file and move back to parent dir
os.chdir("Fourth")
# create an empty file
print(os.getcwd())
print()
os.system("touch four.txt")
# move back to parent dir
os.chdir("..")
print(os.getcwd())
print()
# move to the Fifth child dir and create an empty file and move back to parent dir
os.chdir("Fifth")
print(os.getcwd())
print()
# create an empty file
os.system("touch five.txt")
# move back to parent dir
os.chdir("..")
print(os.getcwd())
print()
