from Bio.Seq import Seq
infile = "/path/gene.fna"
outfile = "/path/dna_seq.txt"
outfile1 = "/path/mrna_seq.txt"
outfile2 = "/path/protein_seq.txt"
with open(infile, 'r') as input_file, \
     open(outfile, 'w') as dna_file, \
     open(outfile1, 'w') as mrna_file, \
     open(outfile2, 'w') as protein_file:
    dna_sequence = ""
    for line in input_file:
        if line.startswith(">"):
            continue
        dna_sequence += line.strip()
    dna_seq = Seq(dna_sequence)
    dna_file.write(str(dna_seq))
    mrna_seq = dna_seq.transcribe()
    mrna_file.write(str(mrna_seq))
    protein_seq = mrna_seq.translate()
    protein_file.write(str(protein_seq))

print("DNA, mRNA, and protein sequences have been written successfully.")
