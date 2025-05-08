from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem.Draw.rdMolDraw2D import MolDraw2DCairo
from sys import argv
from shutil import get_terminal_size

smiles = argv[1]
mol = Chem.MolFromSmiles(smiles)
AllChem.Compute2DCoords(mol)

width, height = get_terminal_size()
drawer = MolDraw2DCairo(width, height)
opts = drawer.drawOptions()

opts.backgroundColour = (0, 0, 0)
opts.useBWAtomPalette()

drawer.DrawMolecule(mol)
drawer.FinishDrawing()

with open("tmp-mol.png","wb") as f:
    f.write(drawer.GetDrawingText())
