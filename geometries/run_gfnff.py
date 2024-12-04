import os
import shutil
import time

geom_2d = "/home/cairne/WorkProjects/SmartChemDesign/logK_hardness_paper/geometries_xtb/ligands_2d"
geom_3d = "/home/cairne/WorkProjects/SmartChemDesign/logK_hardness_paper/geometries_xtb/ligands_gfnff"

mols_to_process = os.listdir(geom_2d)
for mol in mols_to_process:
    mol = mol.replace("(", "\(").replace(")", "\)")
    path_to_mol = os.path.join(geom_2d, mol)
    os.system(f"xtb {path_to_mol} --gfn 2 --sp")
    shutil.copy(os.path.join(geom_2d, "xtbtopo.sdf"),
                os.path.join(geom_3d, mol))

