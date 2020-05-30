import pymol,os

def measure_dst_ang_dihe(pdb_file,protein_name,CST_A_chain_name,CST_A_residue_ID,CST_A_residue_name,Atom_A1,Atom_A2,Atom_A3,CST_B_chain_name,CST_B_residue_ID,CST_B_residue_name,Atom_B1,Atom_B2,Atom_B3):
	pymol.finish_launching()
	from pymol import cmd
	cmd.load(pdb_file,protein_name)

	global A1
	A1='/'+protein_name+'//'+CST_A_chain_name+'/'+CST_A_residue_name+'`'+CST_A_residue_ID+'/'+Atom_A1
	global B1
	B1='/'+protein_name+'//'+CST_B_chain_name+'/'+CST_B_residue_name+'`'+CST_B_residue_ID+'/'+Atom_B1
	global A2
	A2='/'+protein_name+'//'+CST_A_chain_name+'/'+CST_A_residue_name+'`'+CST_A_residue_ID+'/'+Atom_A2
	global B2
	B2='/'+protein_name+'//'+CST_B_chain_name+'/'+CST_B_residue_name+'`'+CST_B_residue_ID+'/'+Atom_B2
	global A3
	A3='/'+protein_name+'//'+CST_A_chain_name+'/'+CST_A_residue_name+'`'+CST_A_residue_ID+'/'+Atom_A3
	global B3
	B3='/'+protein_name+'//'+CST_B_chain_name+'/'+CST_B_residue_name+'`'+CST_B_residue_ID+'/'+Atom_B3

	global dst_AB
	dst_AB = cmd.get_distance(A1,B1)
	global ang_A
	ang_A = cmd.get_angle(A2,A1,B1)
	global ang_B
	ang_B = cmd.get_angle(A1,B1,B2)

	global dihe_A
	dihe_A = cmd.get_dihedral(A3,A2,A1,B1)
	global dihe_AB
	dihe_AB = cmd.get_dihedral(A2,A1,B1,B2)
	global dihe_B
	dihe_B = cmd.get_dihedral(A1,B1,B2,B3)
	cmd.quit()
	
#	return A1,A2,A3,B1,B2,B3,dst_AB,ang_A,ang_B,dihe_A,dihe_AB,dihe_B,pdb_file,protein_name,CST_A_chain_name,CST_A_residue_ID,CST_A_residue_name,Atom_A1,Atom_A2,Atom_A3,CST_B_chain_name,CST_B_residue_ID,CST_B_residue_name,Atom_B1,Atom_B2,Atom_B3
#	return measure_dst_ang_dihe(pdb_file,protein_name,CST_A_chain_name,CST_A_residue_ID,CST_A_residue_name,Atom_A1,Atom_A2,Atom_A3,CST_B_chain_name,CST_B_residue_ID,CST_B_residue_name,Atom_B1,Atom_B2,Atom_B3)
	
	
def write_cst_head(outfile_name,protein_name,CST_A_residue_ID,CST_A_residue_name,CST_B_residue_ID,CST_B_residue_name):
	global outfi
	outfi = open(outfile_name,'w')
	
	outfi.write('# cst constraint descriptior for '+ protein_name +'\n\n\n')
	outfi.write('# NOTE\n\n\n')
	outfi.write('# block 1 for residue '+CST_A_residue_ID+' '+CST_A_residue_name+' and residue '+CST_B_residue_ID+' '+CST_B_residue_name+'\n\n')
	outfi.write('CST::BEGIN\n')
def write_cst_template():
	outfi.write('  TEMPLATE::   ATOM_MAP: 1 atom_name: '+A1.split('/')[-1]+' '+A2.split('/')[-1]+' '+A3.split('/')[-1]+' '+'\n')
	outfi.write('  TEMPLATE::   ATOM_MAP: 1 residue3: '+A1.split('/')[-2].split('`')[0]+'\n\n')
	outfi.write('  TEMPLATE::   ATOM_MAP: 2 atom_name: '+B1.split('/')[-1]+' '+B2.split('/')[-1]+' '+B3.split('/')[-1]+' '+'\n')
	outfi.write('  TEMPLATE::   ATOM_MAP: 2 residue3: '+B1.split('/')[-2].split('`')[0]+'\n\n')
def write_cst_constraint_distanceAB(CST1,CST2):
	outfi.write('  CONSTRAINT:: distanceAB: '+ "%6.2f"%dst_AB +  ' '+ "%4.2f"%CST1+' '+"%3.1f"%CST2+'   0    \n')
def write_cst_constraint_angle_A(CST1,CST2,CST3,CST4):
	outfi.write('  CONSTRAINT::    angle_A: '+ "%6.1f"%ang_A +   ' '+"%-4.1f"%CST1+' '+"%3.1f"%CST2+'  '+"%-3.1f"%CST3+' '+CST4+'\n')
def write_cst_constraint_angle_B(CST1,CST2,CST3,CST4):
	outfi.write('  CONSTRAINT::    angle_B: '+ "%6.1f"%ang_B +   ' '+"%-4.1f"%CST1+' '+"%3.1f"%CST2+'  '+"%-3.1f"%CST3+' '+CST4+'\n')
def write_cst_constraint_dihe_A(CST1,CST2,CST3,CST4):
	outfi.write('  CONSTRAINT::  torsion_A: '+ "%6.1f"%dihe_A +  ' '+"%-4.1f"%CST1+' '+"%3.1f"%CST2+'  '+"%-3.1f"%CST3+' '+CST4+'\n')
def write_cst_constraint_dihe_AB(CST1,CST2,CST3,CST4):
	outfi.write('  CONSTRAINT:: torsion_AB: '+ "%6.1f"%dihe_AB + ' '+"%-4.1f"%CST1+' '+"%3.1f"%CST2+'  '+"%-3.1f"%CST3+' '+CST4+'\n')
def write_cst_constraint_dihe_B(CST1,CST2,CST3,CST4):
	outfi.write('  CONSTRAINT::  torsion_B: '+ "%6.1f"%dihe_B +  ' '+"%-4.1f"%CST1+' '+"%3.1f"%CST2+'  '+"%-3.1f"%CST3+' '+CST4+'\n')
def write_cst_end():
	outfi.write('CST::END\n\n\n')
	outfi.close()
def write_cst_template_new_ligand(Atom_info):
	if 'type' in Atom_info:
		outfi.write('  TEMPLATE::   ATOM_MAP: 1 atom_type: ' + Atom_info.split(':')[-1] + '\n')
	if 'name' in Atom_info:
		outfi.write('  TEMPLATE::   ATOM_MAP: 1 atom_name: ' + Atom_info.split(':')[-1] + '\n')
	outfi.write('  TEMPLATE::   ATOM_MAP: 1 residue3: ' + design_ligand_name + '\n\n')
	outfi.write('  TEMPLATE::   ATOM_MAP: 2 atom_name: '+B1.split('/')[-1]+' '+B2.split('/')[-1]+' '+B3.split('/')[-1]+' '+'\n')
	outfi.write('  TEMPLATE::   ATOM_MAP: 2 residue3: '+B1.split('/')[-2].split('`')[0]+'\n\n')

def main():
	measure_dst_ang_dihe(input_pdb,pdbname,CST_A_chain_name,CST_A_residue_ID,CST_A_residue_name,Atom_A1,Atom_A2,Atom_A3,CST_B_chain_name,CST_B_residue_ID,CST_B_residue_name,Atom_B1,Atom_B2,Atom_B3)
	write_cst_head(pdbname+'.cst',pdbname,CST_A_residue_ID,CST_A_residue_name,CST_B_residue_ID,CST_B_residue_name)
	if design_ligand_name == 'ABC':
		write_cst_template_new_ligand(Atom_info)
	else:
		write_cst_template()
	write_cst_constraint_distanceAB(0.2,100.0)
	write_cst_constraint_angle_A(float(10.0),60.0,360.0,'')
	write_cst_constraint_angle_B(10.0,60.0,360.0,'')
	write_cst_constraint_dihe_A(10.0,60.0,360.0,'')
	write_cst_constraint_dihe_AB(10.0,60.0,360.0,'')
	write_cst_constraint_dihe_B(10.0,60.0,360.0,'')
	write_cst_end()
	os.system('cp ' + pdbname + '.cst match.cst')

if __name__ == '__main__':
	input_pdb = '1D6N_A68K_G102K_F35L_renumber.pdb'
	pdbname = input_pdb.split('.pdb')[0]
	CST_A_chain_name = 'A'
	CST_A_residue_ID = '216'
	CST_A_residue_name = 'PRP'
	Atom_A1 = 'O2B'
	Atom_A2 = 'PB'
	Atom_A3 = 'O3A'
	CST_B_chain_name = 'A'
	CST_B_residue_ID = '131'
	CST_B_residue_name = 'ASP'
	Atom_B1 = 'OD2'
	Atom_B2 = 'CG'
	Atom_B3 = 'CB'
	##attentions
	##when these atoms Atom_A1, Atom_A2, Atom_A3 do not in designed ligand 'ABC', we should add some more information about these Atoms aligned to the reference ligand.
	##for example in this study, we want to design a binding between one 'OH' group and '-COOH' group on ASP
	##in this example, the 'PRP' is a reference ligand, so we add some atom informations below
	##more inofrmation see ROSETTA software about enzymematch and enzymedesign cst file
	Atom_info = 'type:OH'           #or use the atom name like this: Atom_info = 'name:OD2 CG CB'
	design_ligand_name = 'ABC'      ##default 'ABC', record easily, if users do not use a reference ligand, please comment these two lines out
	########attentions out
	main()

