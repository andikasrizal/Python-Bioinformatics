from rdkit import Chem
from rdkit.Chem import Draw
smile="C1CN(CCN1CCOCC(=O)O)C(C2=CC=CC=C2)C3=CC=C(C=C3)Cl.Cl.Cl"
cd=Chem.MolFromSmiles(smile)
for atom in cd.GetAtoms():
    atom.SetProp("molAtomMapNumber",str(atom.GetIdx()))
ls=Draw.MolToFile(cd,'a.png',size=(800,800))