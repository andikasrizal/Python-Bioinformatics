def build_codon_table():
    codon_table = {}
    codon_table['UUU'] = 'F'
    codon_table['UUC'] = 'F'
    codon_table['UUA'] = 'L'
    codon_table['UUG'] = 'L'
    codon_table['CUU'] = 'L'
    codon_table['CUC'] = 'L'
    codon_table['CUA'] = 'L'
    codon_table['CUG'] = 'L'
    codon_table['AUU'] = 'I'
    codon_table['AUC'] = 'I'
    codon_table['AUA'] = 'I'
    codon_table['AUG'] = 'M'
    codon_table['GUU'] = 'V'
    codon_table['GUC'] = 'V'
    codon_table['GUA'] = 'V'
    codon_table['GUG'] = 'V'
    codon_table['UCU'] = 'S'
    codon_table['UCC'] = 'S'
    codon_table['UCA'] = 'S'
    codon_table['UCG'] = 'S'
    codon_table['AGU'] = 'S'
    codon_table['AGC'] = 'S'
    codon_table['CCU'] = 'P'
    codon_table['CCC'] = 'P'
    codon_table['CCA'] = 'P'
    codon_table['CCG'] = 'P'
    codon_table['ACU'] = 'T'
    codon_table['ACC'] = 'T'
    codon_table['ACA'] = 'T'
    codon_table['ACG'] = 'T'
    codon_table['GCU'] = 'A'
    codon_table['GCC'] = 'A'
    codon_table['GCA'] = 'A'
    codon_table['GCG'] = 'A'
    codon_table['UAU'] = 'Y'
    codon_table['UAC'] = 'Y'
    codon_table['CAU'] = 'H'
    codon_table['CAC'] = 'H'
    codon_table['CAA'] = 'Q'
    codon_table['CAG'] = 'Q'
    codon_table['AAU'] = 'N'
    codon_table['AAC'] = 'N'
    codon_table['AAA'] = 'K'
    codon_table['AAG'] = 'K'
    codon_table['GAU'] = 'D'
    codon_table['GAC'] = 'D'
    codon_table['GAA'] = 'E'
    codon_table['GAG'] = 'E'
    codon_table['UGU'] = 'C'
    codon_table['UGC'] = 'C'
    codon_table['UGG'] = 'W'
    codon_table['CGU'] = 'R'
    codon_table['CGC'] = 'R'
    codon_table['CGA'] = 'R'
    codon_table['CGG'] = 'R'
    codon_table['AGA'] = 'R'
    codon_table['AGG'] = 'R'
    codon_table['GGU'] = 'G'
    codon_table['GGC'] = 'G'
    codon_table['GGA'] = 'G'
    codon_table['GGG'] = 'G'
    codon_table['UAA'] = '*'
    codon_table['UAG'] = '*'
    codon_table['UGA'] = '*'
    return codon_table


def transcribe_dna_to_rna(dna_seq):
    seq = dna_seq.upper()
    seq = seq.replace(" ", "")
    seq = ''.join([c for c in seq if c.isalpha()])
    rna_seq = seq.replace('T', 'U')
    return rna_seq


def translate_rna(rna_seq, codon_table, from_start_codon=False):
    seq = rna_seq.upper()
    seq = seq.replace(" ", "")
    seq = ''.join([c for c in seq if c in ('A', 'U', 'G', 'C')])

    if from_start_codon:
        start_index = seq.find('AUG')
        if start_index == -1:
            return ''
        seq = seq[start_index:]

    protein_chars = []
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i+3]
        aa = codon_table.get(codon, 'X')
        if aa == '*':
            break
        protein_chars.append(aa)

    return ''.join(protein_chars)


if __name__ == '__main__':
    table = build_codon_table()
    example_rna = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    protein1 = translate_rna(example_rna, table, from_start_codon=False)
    print("Protein (frame 0):", protein1)

    protein2 = translate_rna(example_rna, table, from_start_codon=True)
    print("Protein (from first AUG):", protein2)

    example_dna = "ATGGCCATGGCGCCCAGAACCTGAGATCAATAGTACCCGTATTAACGGGTGA"
    rna_from_dna = transcribe_dna_to_rna(example_dna)
    protein3 = translate_rna(rna_from_dna, table, from_start_codon=True)
    print("Protein (from DNA -> transcribed -> AUG):", protein3)

    bad_rna = "AUGGXX"
    protein4 = translate_rna(bad_rna, table, from_start_codon=False)
    print("Protein (bad input):", protein4)
