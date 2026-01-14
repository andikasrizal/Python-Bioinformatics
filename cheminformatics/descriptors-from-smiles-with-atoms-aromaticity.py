from rdkit import Chem
from rdkit.Chem import Draw

caffeine_smiles = "Cn1cnc2n(C)c(=O)n(C)c(=O)c12"

mol = Chem.MolFromSmiles(caffeine_smiles)
if mol is None:
    raise ValueError("Invalid SMILES")

for atom in mol.GetAtoms():
    atom.SetProp("molAtomMapNumber", str(atom.GetIdx()))

Draw.MolToFile(mol, "output_prop.png")

for atom in mol.GetAtoms():
    print(atom.GetIdx(), atom.GetAtomicNum(), atom.GetIsAromatic(), atom.GetSymbol())

for bond in mol.GetBonds():
    print(bond.GetBeginAtomIdx(), bond.GetEndAtomIdx(), bond.GetBondType())
