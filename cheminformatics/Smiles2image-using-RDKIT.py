from rdkit import Chem
from rdkit.Chem import Draw
from PIL import Image
smiles="CC(=O)OC1=CC=CC=C1C(=O)O"
m=Chem.MolFromSmiles(smiles)
img=Draw.MolToImage(m,size=(400,400))
output_file="mol.png"
img.save(output_file)
img.show()
