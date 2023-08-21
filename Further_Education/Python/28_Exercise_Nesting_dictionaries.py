"""
16.02.2023
Created by: Jessica Göckler
- Write a program that creates a complex dictionary in form of a
  protein collection
- Each key of the dictionary "proteins" should be associated with another
  dictionary as value in which the name, the length of the protein,
  the function and the location are collected
- The final dictionary should contain information of at least four proteins
- Print out the final dictionary at the end
"""
dictionary1 = {}
dictionary1["Protein1"] = {"Name": "Collagen I", "Length": 54, "Function": "Building Fibrilles", "Location": "Human Body"}
dictionary1["Protein2"] = {"Name": "Albumin", "Length": 585, "Function": "binding", "Location": "Blood"}
dictionary1["Protein3"] = {"Name": "Histone", "Length": 146, "Function": "Regulation", "Location": "Nucleus"}
dictionary1["Protein4"] = {"Name": "Alanine transaminase", "Length": 495, "Function": "na", "Location": "Blood"}


print()
print(dictionary1)
print()
print(dictionary1["Protein1"])
print()
print(dictionary1["Protein2"]["Length"])
