from Bio.Seq import Seq
Seq1=Seq("ATY")
Seq2=Seq("GRC")
t1=Seq1.translate()
t2=Seq2.translate()
print("The translated sequence of ATY is :",t1)
print("The translated sequence of GRC is :",t2)