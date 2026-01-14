from rdkit import Chem
from rdkit.Chem import Draw
import pandas as pd

smile="C1CN(CCN1CCOCC(=O)O)C(C2=CC=CC=C2)C3=CC=C(C=C3)Cl.Cl.Cl"
mol=Chem.MolFromSmiles(smile)
for atom in mol.GetAtoms():
    atom.SetProp("molAtomMapNumber",str(atom.GetIdx()))
of=('aafinal.png')
Draw.MolToFile(mol,of,size=(800,800))

dp=pd.DataFrame({
    'Atomic Index':[atom.GetIdx() for atom in mol.GetAtoms()],
    'Atomic Number':[atom.GetAtomicNum() for atom in mol.GetAtoms()],
    'Is Aromatic':[atom.GetIsAromatic() for atom in mol.GetAtoms()],
    'Atomic Symbol':[atom.GetSymbol() for atom in mol.GetAtoms()]
})
dp.to_excel('random.xlsx',index=True)