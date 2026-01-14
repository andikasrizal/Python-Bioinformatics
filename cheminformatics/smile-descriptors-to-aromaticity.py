from rdkit import Chem
from rdkit.Chem import Draw
from PIL import Image
smiles="C1CN(CCN1CCOCC(=O)O)C(C2=CC=CC=C2)C3=CC=C(C=C3)Cl.Cl.Cl"
mol=Chem.MolFromSmiles(smiles)
for atoms in mol.GetAtoms():
    atoms.SetProp('molAtomMapNumber',str(atoms.GetIdx()))

Draw.MolToFile(mol,'aromaticity1.png')

for atoms in mol.GetAtoms():
    print(atoms.GetIdx(),atoms.GetAtomicNum,atoms.GetIsAromatic,atoms.GetSymbol)
    
for bond in mol.GetBonds():
    print(bond.GetBeginAtomIdx(),bond.GetEndAtomIdx(),bond.GetBondType())