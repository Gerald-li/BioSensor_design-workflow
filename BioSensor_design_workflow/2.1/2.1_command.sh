#!/usr/bin/env bash
##copy the '*_renumber.pdb' file to this directory from 1.2 step or protein_renumber step
cp ../1.2/*_renumber.pdb ./

##execute 2.1_rosetta_protein_prep.py
##all the parameters in the main function of this script need to be replaced according to each protein
python 2.1_rosetta_protein_prep.py

##copy the '*.params' and '*confs.pdb' files created in 1.1 step and the 'match.cst' file created in 1.2 step to 'inputs' directory
cp ../1.1/*.params ./inputs/
cp ../1.1/*confs.pdb ./inputs/
cp ../1.2/match.cst ./inputs/

#execute Rosetta Match model
$ROSETTA_HOME/bin/match.linuxgccrelease @match_out.flags -database $ROSETTA_DATABASE