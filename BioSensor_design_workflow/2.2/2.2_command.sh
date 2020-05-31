#!/usr/bin/env bash
##attentions
##all the parameters in this step scripts need to be replaced according to each project
##according to match result and copy some match result to this directory used to design
#for example:
#cp ../2.1/UM_*_match*.pdb ./


##copy 'ligand params' and '_confs.pdb' files from 1.1 step to this directory and rename it 'design_**.params'
cp ../1.1/ABC.params design_ABC.params
cp ../1.1/ABC_confs.pdb ./

##copy 'match.cst' file from 1.2 step to this directory and rename it 'design.cst'
##design.cst file can be same as match.cst and can be different with match.cst
##more information see ROSETTA software about match and design cst file
cp ../1.2/match.cst design.cst

##creat the design flag file, more information see ROSETTA software about design flag file
python get_design_flags.py

##execute Enzyme Design model
python design_command.py
