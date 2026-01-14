from Bio.Seq import Seq
import matplotlib.pyplot as plt 
with open('dna_seq.txt','r') as f1, open('countoutput.txt','w') as f2:
    for line in f1:
        seq=line.strip()
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
        print(f" Percentage of A is : {perA:.2f}%")
        print(f"\n Percentage of A is : {perT:.2f}%")
        print(f"\n Percentage of A is : {perG:.2f}%")
        print(f"\n Percentage of A is : {perC:.2f}%")
        f2.write(f"\n Percentage of A is : {perA:.2f}%")
        f2.write(f"\n Percentage of T is : {perT:.2f}%")
        f2.write(f"\n Percentage of G is : {perG:.2f}%")
        f2.write(f"\n Percentage of C is : {perC:.2f}%\n\n")
        
        percentages = {
            "A": (CountA / n) * 100,
            "T": (CountT / n) * 100,
            "G": (CountG / n) * 100,
            "C": (CountC / n) * 100
        }

        plt.bar(percentages.keys(), percentages.values(), color=['red', 'blue', 'green', 'orange'])
        plt.title("Nucleotide Percentage Composition (BioPython)")
        plt.xlabel("Nucleotides")
        plt.ylabel("Percentage (%)")
        plt.ylim(0, 100)
        plt.show()