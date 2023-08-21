"""
16.02.2023
Created by: Jessica Göckler
- Create one dictionary xonsisting of at least three pre-defined entries
  with biological or biochemical backround
- Print out and aferwards insert and remove keys/values
- print out the remaining dictionary
"""
dictionary1 = {"Mitochondria":"Nucleus","7+6":13,"Pi":3.14}
print(dictionary1)
# adding
dictionary1["Potassium"] = 19
print(dictionary1)
# deleting
del dictionary1["7+6"]
print(dictionary1)

print(list(dictionary1.keys()))
print(list(dictionary1.values()))
