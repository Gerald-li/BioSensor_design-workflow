#!/usr/bin/env bash

##all the parameters in the main function of this script need to be replaced according to each protein
python 1.2_get_cst_def.py

##after got .cst file, users can use this command to check the cst file
#$ROSETTA_HOME/bin/CstfileToTheozymePDB.linuxgccrelease @cst-to-pdb-flags -database $ROSETTA_DATABASE
#more information see ROSETTA software about cst to pdb