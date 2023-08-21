"""
24.02.2023
Created by: Jessica Göckler
Class Gene 3
- Add a String-method to your class, so that the contents of your objects
  can be printed out in a good manor
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
        print(f"It also has {self.__Nr_ReadingFrame} reading frames and the position is {self._ReadingFrame} \n")
# # Exercise 3
#-------------------------------------------------------------------------------
    def __str__(self):
        printout1 = f"""Printout! A gene with the name {self.__Name}.
The gene has {self.__Nr_Nucleotide} nucleotides and the position {self._Nucleotide} .
It also has {self.__Nr_ReadingFrame} reading frames and the position is {self._ReadingFrame} \n"""
        return printout1
#-------------------------------------------------------------------------------
new_gene1 = Gene("NS5B", 500, 2, 250, 1)
new_gene2 = Gene("NS3", 300, 4, 50, 2)

print(new_gene1)
print(new_gene2)

new_gene1.print_state()      # Part 2 of Exercise 2!
print(new_gene1.get_Name())
print(new_gene1.get_Nr_Nucleotide())
print(new_gene1.get_Nr_ReadingFrame())
print(new_gene1.get_Nucleotide())
print(new_gene1.get_ReadingFrame())
print()
new_gene2.print_state()
print(new_gene2.get_Name())
print(new_gene2.get_Nr_Nucleotide())
print(new_gene2.get_Nr_ReadingFrame())
print(new_gene2.get_Nucleotide())
print(new_gene2.get_ReadingFrame())
