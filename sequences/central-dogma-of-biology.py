from Bio.Seq import Seq
input="/path/filename.fna"
outfile="/path/outputfile.txt"
with open(input,'r') as infile:
    temp_seq=""
    for line in infile:
        if line.startswith(">"):
            continue
        temp_seq+=line.strip()
dna_seq=Seq(temp_seq)
rcomp=dna_seq.reverse_complement()
mrna=rcomp.transcribe()
protein=mrna.translate()
with open(outfile,'w') as out:
    out.write(str(protein))