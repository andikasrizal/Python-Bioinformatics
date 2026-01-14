from Bio.Seq import Seq
infile = "/path/infile.fna"
outfile = "/path/dna2_seq.txt"
outfile1 = "/path/mrna2_seq.txt"
outfile2 = "/path/protein2_seq.txt"
with open(infile, 'r') as input_file, \
     open(outfile, 'w') as dna2_file, \
     open(outfile1, 'w') as mrna2_file, \
     open(outfile2, 'w') as protein2_file:
    dna_sequence = ""
    for line in input_file:
        if line.startswith(">"):
            continue
        dna_sequence += line.strip()

    dna_seq = Seq(dna_sequence)
    dna_sss=dna_seq.reverse_complement()
    
    dna2_file.write(str(dna_sss))
    mrna_seq = dna_sss.transcribe()
    
    mrna2_file.write(str(mrna_seq))
    protein_seq = mrna_seq.translate()
    protein2_file.write(str(protein_seq))

print("DNA, mRNA, and protein sequences have been written successfully.")
