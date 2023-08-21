"""
24.02.2023
Created by: Jessica Göckler
- Expand the class from the first exercise by adding several methods to it.
  - One getter() for each attribute defined in the class
  - The methods up_nucleotide(), down_nucleotide(), up_readingframe() and
    down_readingframe() that allow the user to change the nucleotide and
    readingframe accordingly but only if possible
  - A method print_state() tat prints out the name of the gene the used
    nucleotide and the used ReadingFrame
"""
class Gene():
    def __init__(self, Name, Nr_Nucleotide, Nr_ReadingFrame, Nucleotide, ReadingFrame):
        self.__Name = Name
        self.__Nr_Nucleotide = Nr_Nucleotide
        self.__Nr_ReadingFrame = Nr_ReadingFrame
        self._Nucleotide = Nucleotide
        self._ReadingFrame = ReadingFrame

    def get_Name(self):
        return self.__Name

    def get_Nr_Nucleotide(self):
        return self.__Nr_Nucleotide

    def get_Nr_ReadingFrame(self):
        return self.__Nr_ReadingFrame

    def get_Nucleotide(self):
        return self._Nucleotide

    def get_ReadingFrame(self):
        return self._ReadingFrame

    def up_nucleotide(self):
        self._Nucleotide += 1

    def down_nucleotide(self):
        self._Nucleotide -= 1

    def up_readingframe(self):
        self._ReadingFrame += 1

    def down_readingframe(self):
        self._ReadingFrame -= 1
# Bis hier hin eigenständig gelöst
#-------------------------------------------------------------------------------
    def print_state(self):
        print(f"A gene with the name {self.__Name}")
        print(f"The gene has {self.__Nr_Nucleotide} nucleotides and the position {self._Nucleotide}")
        print(f"It also has {self.__Nr_ReadingFrame} reading frames and the position is {self._ReadingFrame}")

new_gene1 = Gene('NS5B', 500, 2, 250, 1)
new_gene2 = Gene("NS3", 300, 4, 50, 2)

new_gene1.
print(new_gene1)
print(type(new_gene1))
