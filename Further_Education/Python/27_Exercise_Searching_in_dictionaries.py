"""
16.02.2023
Created by: Jessica Göckler
- Create a dictionary with at least 10 entries with biological or biochemical
  background
- Search the dictionary for a specific key
- If the key is already present update the value for this key, if the key does
  not exist add it to the dictionary
- Run this option at least 3 times during one call of the program
- Print out the original dictionary at the beginning an the modified dictionary
  at the end.
"""
dictionary1 = {"Nucleus":"Nucleolus",
                "Nuclear Membrane":"Cytoplasm",
                "Golgi":"Mitochondrion",
                "Ribosomes":"Ribosomes",
                "Endoplaspatic reticulum":"Chloroplast",
                "Cytoplasmatic Membrane":"Eucaryotic Cell",
                "Cytosine":"C",
                "Guanine":"G",
                "Thymine":"T",
                "Adenine":"A",}
print()
if "Pi" in dictionary1:
    print("It is part of your dictionary. ")
else:
    dictionary1["Pi"] = 3.14
    print(dictionary1)
print()
if "Numpy" in dictionary1:
    print("It is part of your dictionary. ")
else:
    dictionary1["Numpy"] = "Programming language"
    print(dictionary1)
print()
if "Thymine" in dictionary1:
    print("It is part of your dictionary. ")
else:
    dictionary1["Thymine"] = "Escherichia coli"
    print(dictionary1)
print()
print(list(dictionary1.keys()))
print(list(dictionary1.values()))
