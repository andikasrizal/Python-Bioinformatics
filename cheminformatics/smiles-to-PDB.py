from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import PDBWriter
smiles="CC(=O)OC1=CC=CC=C1C(=O)O"
m=Chem.MolFromSmiles(smiles)
AllChem.EmbedMolecule(m)
output_file="output.pdb"
with PDBWriter(output_file) as writer:
    writer.write(m)
