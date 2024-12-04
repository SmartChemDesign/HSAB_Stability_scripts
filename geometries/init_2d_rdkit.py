import os
from rdkit import Chem
from rdkit.Chem import AllChem

main_folder = "/home/cairne/WorkProjects/logK_hardness_paper/geometries/complexes_2d"
files = os.listdir(main_folder)

for file in files:
    path_to_sdf = os.path.join(main_folder, file)
    mol = Chem.SDMolSupplier(path_to_sdf, removeHs=False)[0]
    AllChem.Compute2DCoords(mol)
    writer = Chem.SDWriter(path_to_sdf)
    writer.write(mol)
