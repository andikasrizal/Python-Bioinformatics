def conversion(sequence):
    conversion = ""
    for base in sequence:
        if base=="T":
            conversion+="U"
        elif base=="A":
            conversion+="A"
        elif base=="G":
            conversion+="G"
        elif base=="C":
            conversion+="C"
    return conversion

def  conversiond(sequence):
    conversiond = ""
    for terms in sequence:
        if terms=="T":
            conversiond+="U"
        else:
            conversiond+=terms
    return conversiond

sequence=input("enter sequence : ") 
print(sequence)
print(conversion(sequence))
print(conversiond(sequence))
   