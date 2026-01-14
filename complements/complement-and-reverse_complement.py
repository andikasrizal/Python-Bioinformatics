from Bio.Seq import Seq
my_dna=Seq(input("Enter a sequence :"))
dna=my_dna
complement= my_dna.complement()
reversecomp=my_dna.reverse_complement()
print("Original DNA sequence: ", dna)
print("Complement DNA sequence: ", complement)
print("Reverse complement is :",reversecomp)
