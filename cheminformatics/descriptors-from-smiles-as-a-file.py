from rdkit import Chem
import pandas as pd

caffeine_smiles = 'Cn1cnc2n(C)c(=O)n(C)c(=O)c12'

mol = Chem.MolFromSmiles(caffeine_smiles)

if mol is None:
    raise ValueError("Invalid SMILES string")

df = pd.DataFrame({
    'Atom Index': [atom.GetIdx() for atom in mol.GetAtoms()],
    'Atomic Number': [atom.GetAtomicNum() for atom in mol.GetAtoms()],
    'Atomic Symbol': [atom.GetSymbol() for atom in mol.GetAtoms()],
    'Is Aromatic': [atom.GetIsAromatic() for atom in mol.GetAtoms()]
})
df.to_excel("caffeine_atom_descriptors.xlsx", index=False)
print("Excel file saved successfully!")
