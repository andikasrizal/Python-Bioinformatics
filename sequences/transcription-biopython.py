from Bio.Seq import Seq
sequence=Seq(input("Enter the sequence : "))
print(sequence)
rna_sequence=sequence.transcribe()
print("Original sequence is :",sequence)    
print("Transcribed Sequence is :",rna_sequence)