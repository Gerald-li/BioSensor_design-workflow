import os, sys

def extract_ligand(input_pdbfile):
	with open(input_pdbfile, 'r') as f:
		lines = f.readlines()
	f.close()
	for line in lines:		
#		if line.startswith(('ATOM', 'HETATM', 'ANISOU')):
		if line.startswith(('ATOM', 'HETATM')):
#			print line[21],line[22:26],line[17:20],line[12:16]
			if line[21] == ligand_chain_name and line[22:26].strip() == ligand_ID_name and line[17:20].strip() == ligand_name:
#				print line
				out_pdbfile.write(line)
		else:
			continue

	out_pdbfile.write('TER\nEND\n')
	out_pdbfile.close()
input_pdbfile = sys.argv[1]
pdbname = sys.argv[1].split('.pdb')[0]
out_pdbfile = open(sys.argv[1].split('.pdb')[0]+'_chain'+sys.argv[2]+'_'+sys.argv[3]+'_'+sys.argv[4]+'.pdb','w')
ligand_chain_name = sys.argv[2]
ligand_ID_name = sys.argv[3]
ligand_name = sys.argv[4]


#s = parser.get_structure('1gm9', './1gm9.pdb')

#io.save('1gm9_chainB_1569_SOX.pdb', LigandSelect('B', 1569, 'SOX'))
#io.save(out_pdbfile, LigandSelect(ligand_chain_name, ligand_ID_name, ligand_name))
#io.save('1gm9_noHETATM.pdb',ChainSelect('A'))
extract_ligand(input_pdbfile)
