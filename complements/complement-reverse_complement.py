from Bio.Seq import Seq
def random (Seqn):
    var=""
    if(random=="A"):
        var+="T"
    elif(random=="T"):
        var+="A"
    elif(random=="G"):
        var+="C"
    elif(random=="C"):
        var+="G"
        return var
Seqn=Seq(input("Enter a sequence  : "))
print("Changed complement is:",random(Seqn))
srv=Seqn
a=reversed(srv)
print("Reversed is : ",a)
    