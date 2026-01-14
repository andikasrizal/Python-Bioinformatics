from rdkit import Chem
from rdkit.Chem import AllChem,Draw,PDBWriter,DataStructs,Descriptors
smile="C1CN(CCN1CCOCC(=O)O)C(C2=CC=CC=C2)C3=CC=C(C=C3)Cl.Cl.Cl"
mol=Chem.MolFromSmiles(smile)
for atom in mol.GetAtoms():
    atom.SetProp("molAtomMapNumber",str(atom.GetIdx()))
of=('apic.png')
Draw.MolToFile(mol,of,size=(800,800))

datastruct={
    'MolecularWeight':Descriptors.MolWt(mol),
    'NumAtoms':Descriptors.HeavyAtomCount(mol),
    'LogP':Descriptors.MolLogP(mol),
    'NumHAcceptors':Descriptors.NumHAcceptors(mol),
    'NumHdonors':Descriptors.NumHDonors(mol)
}

for key, value in datastruct.items():
    print(f"{key}:{value}")