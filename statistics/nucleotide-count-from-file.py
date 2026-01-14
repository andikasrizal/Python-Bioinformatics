from Bio.Seq import Seq
with open('dna_seq.txt','r') as f1, open('countoutput.txt','w') as f2:
    Sequence=f1.readlines()
    for line in Sequence:
        seq=Seq(line.strip())
        CountA=seq.count("A")
        CountT=seq.count("T")
        CountG=seq.count("G")
        CountC=seq.count("C")
        print("Count of A is :",CountA)
        print("Count of T is : ",CountT)
        print("Count of G is : ",CountG)
        print("Count of C is : ",CountC)
        f2.write(f"Count of A is: {CountA}")
        f2.write(f"\n Count of T is : {CountT}")
        f2.write(f"\n Count of G is : {CountG}")
        f2.write(f"\n Count of C is :{CountC}")
        l=len(seq)
        print("Length of Sequence :",l)
        print("\n")
        n=CountA+CountT+CountG+CountC
        perA=(CountA/n)*100
        perT=(CountT/n)*100
        perG=(CountG/n)*100
        perC=(CountC/n)*100
        print("Percentage of A is :",perA)
        print("Percentage of T is : ",perT)
        print("Percentage of G is : ",perG)
        print("Percentage of C is : ",perC)
        f2.write(f"\n Percentage of A is : {perA}")
        f2.write(f"\n Percentage of T is : {perT}")
        f2.write(f"\n Percentage of G is : {perG}")
        f2.write(f"\n Percentage of C is : {perC}\n\n")