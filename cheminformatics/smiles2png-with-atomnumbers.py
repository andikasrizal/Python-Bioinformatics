from rdkit import Chem
from rdkit.Chem import Draw

caffeine_smiles = "CN1C=NC2=C1C(=O)N(C(=O)N2C)C"
m = Chem.MolFromSmiles(caffeine_smiles)

Draw.MolToFile(m, 'caffeine.png')

for atoms in m.GetAtoms():
    atoms.SetProp('MolAtomMapNumber', str(atoms.GetIdx()))

drawer = Draw.MolDraw2DCairo(300, 300)
opts = drawer.drawOptions()
opts.addAtomIndices = True  
drawer.DrawMolecule(m)
drawer.FinishDrawing()
drawer.WriteDrawingText('molatoms_with_index.png')
