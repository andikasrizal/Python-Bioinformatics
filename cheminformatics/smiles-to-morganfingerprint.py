from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import DataStructs

smiles="CC(=O)OC1=CC=CC=C1C(=O)O"
mol=Chem.MolFromSmiles(smiles)
fp=AllChem.GetMorganFingerprintAsBitVect(mol,2) 
print(f"fingerprint : {fp}")

gen = AllChem.GetMorganGenerator(radius=2)
fp2=gen.GetFingerprint(mol)
print(f"fingerprint : {fp2}")

fpl=DataStructs.BitVectToText(fp)
print(f"Finger print :{fpl}")

print("Bit string:", fp.ToBitString()) 
print("Bits set:", fp.GetNumOnBits()) 
