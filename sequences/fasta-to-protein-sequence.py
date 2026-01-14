from Bio.Seq import Seq
infile="/path/gene.fna"
outfile="/path/aram1.txt"
outfile1="/path/aram2.txt"
outfile2="/path/aram3.txt"
with open(infile,'r') as input:
 sequencetemp=""
 for line in input:
     if line.startswith(">"):
         continue
     sequencetemp+=line.strip()
     
 while len(sequencetemp) % 3 != 0:
         sequencetemp += "N"

with open(outfile,'w') as out1,\
     open(outfile1,'w') as out2, \
     open(outfile2,'w') as out3:
     dnaseq=Seq(sequencetemp)
     out1.write(str(dnaseq))
     mrnaseq=dnaseq.transcribe()
     out2.write(str(mrnaseq))
     protein=mrnaseq.translate()
     out3.write(str(protein))


    