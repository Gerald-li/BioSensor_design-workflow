# BioSensor_design workflow
This is a manual for BioSensor_design workflow script and an example
## Three steps for BioSensor_design workflow：
Before the first step, we need to carry out simple pre-processing of protein and have a detailed understanding of the protein. 
These works are very important for researchers to understand their own biosensor system and successful design
#### pre-processing：
（1）Get the PDB structure of the protein (you can search and download it on the PDB bank website http://www.rcsb.org/ )

（2）Understand the possible binding modes and positions of molecules and proteins 
(refer to the binding modes of ligands and proteins in protein crystals, such as hydrogen bonds, salt bridges, etc.)

（3）A renumber pdb file needed beause we need a Constraint_Type file in match and design processes. 

Generally speaking, the Constraint_Type will contain a type, defining what sort of value to be constrained (distance, angle, dihedral, etc), and a series of atom and/or residue labels defining a specific quality to be constrained. Residue numbers are assumed to be in Rosetta numbering (from 1, no gaps), not PDB numbering. (more information in https://www.rosettacommons.org/manuals/archive/rosetta3.5_user_guide/de/d50/constraint_file.html)

### The first step：
（1）Get the conformations of the ligand. （see biosensor_design_workflow/1.1/1.1_README）

（2）Get the Constraint_Type file. （see biosensor_design_workflow/1.2/1.2_README）

### The second step：
（1）Rosetta Match model （see biosensor_design_workflow/2.1/2.1_README）

（2）Rosetta Enzyme Design model （see biosensor_design_workflow/2.2/2.2_README）

### The third step：
（1）Filter results based on parameters, two analysis scripts here can help users easy to use. (see biosensor_design_workflow/2.2/2.2_README)

## In order to run this workflow, some software needed：

（一）**Schrodinger software**，This is a commercial software. If you need it, you can go to Schrodinger's website first（ https://www.schrodinger.com/ ）to obtain a free trial version, and then you need to purchase the license。

（二）**ROSETTA software**，(https://www.rosettacommons.org/) The Rosetta software suite includes algorithms for computational modeling and analysis of protein structures. 
It has enabled notable scientific advances in computational biology, including de novo protein design, enzyme design, ligand docking, and structure prediction of biological macromolecules and macromolecular complexes.
 
（三）**Pymol software**，PyMOL's website（ https://pymol.org/2/ ）。PyMOL is an open source molecular visualization system created by Warren Lyford DeLano.
