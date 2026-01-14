def complement(dna_sequence):
    complement1 = ""
    for base in dna_sequence:
        if base =="A":
            complement1+="T"
        elif base == "T":
            complement1+="A"
        elif base == "C":
            complement1+="G"
        elif base == "G":
            complement1+="C"
    return complement1

dna_sequence = input("Enter DNA Sequence : ")
print(dna_sequence)
print("complement is :",complement(dna_sequence))
print("reverse complement is :",complement(dna_sequence)[::-1]) 
