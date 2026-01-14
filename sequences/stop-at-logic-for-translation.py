from Bio.Seq import Seq
sequence=Seq(input("Enter the DNA sequence"))
mrna=sequence.transcribe()
protein=mrna.translate()
print("The protein : ",protein)
stopp=mrna.translate(to_stop=True)
print("Stop at :",stopp)