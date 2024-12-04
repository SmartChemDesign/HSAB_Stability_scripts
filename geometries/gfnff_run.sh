#!/bin/bash

for FILE  in "complexes_2d"/*; do
#    if [[ -d "$FILE" ]]
#    then
       f="$(basename -- $FILE)"
       echo $f
       xtb complexes_2d/$f --gfn 2 --sp
       cp "gfnff_convert.sdf" $HOME/WorkProjects/SmartChemDesign/logK_hardness_paper/geometries/complexes_gfnff/$f
#    fi
done
