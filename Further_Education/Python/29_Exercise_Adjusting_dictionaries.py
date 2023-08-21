"""
16.02.2023
Created by: Jessica Göckler
- Take your dictionary from exercise 28 and write a program that allows to make
  some changes:
  - use an if statement to differ between adding a key,
    deleting a key or changing the value associated with the key
  - If deleting is executed remove a complete Key/Value pair from the dictionary
  - For changing specify a key of the outer dictionary as well as a Key
    of the inner dictionary
  - For changing specify a key of the outer dictionary as well as a key of
    the inner dictionary and change the value associated with the letter
  - For adding, define all necessary information to fill a complete
    new inner diceionary
"""
dictionary1 = {}
dictionary1["Protein1"] = {"Name": "Colagen", "Length": 54, "Function": "Building Fibrilles", "Location": "Human Body"}
dictionary1["Protein2"] = {"Name": "Thymine", "Length": 585, "Function": "binding", "Location": "Blood"}
dictionary1["Protein3"] = {"Name": "Histone", "Length": 146, "Function": "Regulation", "Location": "Nucleus"}
dictionary1["Protein4"] = {"Name": "Alanine transaminase", "Length": 495, "Function": "na", "Location": "Blood"}
print()
print(dictionary1)
print()
# Musterlösung
# choice = 1
# # Deleting
# if choice == 1:
#     del dictionary1["Protein1"]
# # Changing
# elif choice == 2:
#     dictionary1["Protein2"]["Name"] = "Albumin"
# # Adding
# elif choice == 3:
#     dictionary1["Protein3"] = {"Short":"ALT"}

choice = input("Choose between 1, 2 and 3 specifications for your list: \n"
                "1 = Deleting, \n"
                "2 = Changing, \n"
                "3 = Adding \n")
# Deleting
if choice == "1":
    del dictionary1["Protein1"]
# Changing
elif choice == "2":
    dictionary1["Protein2"]["Name"] = "Albumin"
# Adding
elif choice == "3":
    dictionary1["Protein3"] = {"Name": "Histone", "Length": 146, "Function": "Regulation", "Location": "Nucleus", "Short":"ALT"}

print(dictionary1)
