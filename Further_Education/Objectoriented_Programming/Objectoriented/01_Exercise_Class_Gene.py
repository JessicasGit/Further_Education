"""
24.02.2023
Created by: Jessica Göckler
- Generate our own class called "Gene" that has the following five attributes:
  - __Name: a string (private)
  - __Nr_Nucleotide: a positive whole number (private)
  - __Nr_ReadingFrame: a positive whole number (private)
  - _Nucleotide: a positive whole number (protected)
  - _ReadingFrame: a positive whole number (protected)
  - __Nr_Nucleotide and __Nr_ReadingFrame are the maximum number and
    _Nucleotide and _ReadingFrame are the current number
- All attributes should be given to the constructor of the class if
  a new Object is generated
"""
class Gene():
    def __init__(self, Name, Nr_Nucleotide, Nr_ReadingFrame, Nucleotide, ReadingFrame):
        self.__Name = Name
        self.__Nr_Nucleotide = Nr_Nucleotide
        self.__Nr_ReadingFrame = Nr_ReadingFrame
        self._Nucleotide = Nucleotide
        self._ReadingFrame = ReadingFrame

# Name = "Gene"
# Nr_Nucleotide = 1234
# Nr_ReadingFrame = 345
# Nucleotide = 111
# ReadingFrame = 80

new_gene1 = Gene("NS5B", 500, 2, 250, 1)
new_gene2 = Gene("NS3", 300, 4, 50, 2)
# print(new_gene1, new_gene2)
