from Bio.Seq import Seq          
import os                        
from glob import glob             

input_dir = "/path/input/"
output_dir = "/path/output/"
os.makedirs(output_dir, exist_ok=True)
fna_files = glob(os.path.join(input_dir, "*.fna"))

for infile in fna_files:
    filename = os.path.splitext(os.path.basename(infile))[0]
    dna_out = os.path.join(output_dir, f"{filename}_dna.txt")
    mrna_out = os.path.join(output_dir, f"{filename}_mrna.txt")
    protein_out = os.path.join(output_dir, f"{filename}_protein.txt")
    dna_sequence = ""

    with open(infile, 'r') as input_file:
        for line in input_file:
            if not line.startswith(">"):
                dna_sequence += line.strip()
    dna_seq = Seq(dna_sequence)
    dna_sss = dna_seq.reverse_complement()

    with open(dna_out, 'w') as dna_file, \
         open(mrna_out, 'w') as mrna_file, \
         open(protein_out, 'w') as protein_file:
        dna_file.write(str(dna_sss))
        mrna_seq = dna_sss.transcribe()
        mrna_file.write(str(mrna_seq))
        protein_seq = mrna_seq.translate()
        protein_file.write(str(protein_seq))
    print(f"Processed: {filename}.fna")

print("\nAll .fna files have been processed successfully!")
