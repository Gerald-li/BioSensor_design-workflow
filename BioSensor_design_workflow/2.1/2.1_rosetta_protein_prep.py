import os, sys
def prep_protein(input_pdb, retained_chain, dir_path):
	os.system('prepwizard -watdist 0 -fillsidechains -noepik -s -propka_pH 7.5 -noimpref '+input_pdb+' '+ prep_pdb)
	#for example: prepwizard -watdist 0 -fillsidechains -noepik -s -propka_pH 7.5 -noimpref 1gm9.pdb 1gm9_prep.pdb
	while True:
		if os.path.exists(os.path.join(dir_path, prep_pdb)):
			os.system('sleep 5s')
			break
	os.system('python2 get_noHETATM_protein.py '+input_pdb+' '+retained_chain)
	os.system('python2 get_noHETATM_protein.py '+prep_pdb+' '+retained_chain)
	#for example: python2 get_noHETATM_protein.py 1gm9_prep.pdb AB

def get_ligand(prep_pdb,ligand_chain,ligand_id,ligand_name):
	os.system('python2 extract_ligand.py '+prep_pdb+' ' +ligand_chain+' ' +ligand_id+' '+ligand_name)
	#for example: python2 extract_ligand.py 1gm9_prep.pdb B 1569 SOX

def combi_pdb(first_pdb,second_pdb):
	os.system('python2 change_chain_name_and_combi.py '+first_pdb+' '+second_pdb)
	#for example: python2 change_chain_name_and_combi.py 1gm9_prep_chainAB.pdb 1gm9_prep_chainB_1568_CA.pdb

def get_grid(match_grid):
	if not os.path.exists('inputs'):
		os.mkdir('inputs')
	os.system('cp '+prep_name+'_chain'+res_ligand_chain+'_'+res_ligand_ID+'_'+res_ligand_name+'.pdb ./inputs')
	command = "sed -e 's/nohet.pdb/"+prep_name+"_chain"+res_chain+".pdb/g' -e 's/ligand.pdb/"+prep_name+"_chain"+res_ligand_chain+"_"+res_ligand_ID+"_"+res_ligand_name+".pdb/g' " + match_grid+" > ./match_grid_out.flags"
	os.system(command)
	os.system('$ROSETTA_HOME/bin/gen_lig_grids.linuxgccrelease -database $ROSETTA_DATABASE @match_grid_out.flags')

def get_match_flags(match_flags):
	if not os.path.exists('inputs'):
		os.mkdir('inputs')
	os.system('cp '+prep_name+'_chain'+res_chain+'.pdb ./inputs')
#	os.system('cp '+prep_name+'_chain'+res_chain+'.pdb_0.gridlig ./inputs')
#	os.system('cp '+prep_name+'_chain'+res_chain+'.pdb_0.pos ./inputs')
	command = "sed -e 's/nohet.pdb/"+prep_name+"_chain"+res_chain+".pdb/g' -e 's/@@@/"+design_ligand_name+"/g' -e 's/grid_file/"+prep_name+"_chain"+res_chain+".pdb_0.gridlig/g' -e 's/list_pos_file/"+prep_name+"_chain"+res_chain+".pdb_0.pos/g' match.flags > match_out.flags"
	os.system(command)
	os.system('cp match_out.flags ./inputs')

def change_pos(input_posfile, cat_ID):
	command_bk = 'cp '+ input_posfile +' ' + input_posfile + '_bk'
	os.system(command_bk)
	fi = open(input_posfile,'w')
	fi.write(cat_ID)
	fi.close()

def main():
	prep_protein(input_pdb,res_chain,'./')
	get_ligand(prep_pdb,res_ligand_chain,res_ligand_ID,res_ligand_name)
	step = 0
	if len(other_ligands) < 3:
		print 'There are no ligands that need to be retained'
	else:
		print 'Retained ligands : '+ str(other_ligands)
		for i in other_ligands:
			step = step +1
			if step <=3:
				if step % 3 == 0:
					combi_name = str(other_ligands[step-3:step]).split('[')[-1].split(']')[0]
					get_ligand(input_pdb,combi_name.split(',')[0],combi_name.split(',')[1].strip(),combi_name.split(',')[2].strip())
					last_out_name = input_pdb.split('.pdb')[0]+'_chain'+str(combi_name.split(',')[0]).replace('\'','')+'_'+str(combi_name.split(',')[1].strip()).replace('\'','')+'_'+str(combi_name.split(',')[2].strip()).replace('\'','')+'.pdb'
					combi_pdb(input_name+'_chain'+res_chain+'.pdb',last_out_name)
			if step > 3:
				if step % 3 == 0:
					combi_name = str(other_ligands[step-3:step]).split('[')[-1].split(']')[0]
					get_ligand(input_pdb,combi_name.split(',')[0],combi_name.split(',')[1].strip(),combi_name.split(',')[2].strip())
					last_out_name = input_pdb.split('.pdb')[0]+'_chain'+str(combi_name.split(',')[0]).replace('\'','')+'_'+str(combi_name.split(',')[1].strip()).replace('\'','')+'_'+str(combi_name.split(',')[2].strip()).replace('\'','')+'.pdb'
					combi_pdb('combi_ligands.pdb',last_out_name)

	os.system("sed -i '/^TER/c'TER'' combi_ligands.pdb")
	get_match_flags(match_flags)
	get_grid(match_grid)
	os.chdir('inputs')
	change_pos(prep_name+"_chain"+res_chain+".pdb_0.pos", cat_ID)

if __name__ == '__main__':
	match_grid = 'match_grid.flags'
	match_flags = 'match.flags'
	res_ligand_chain = 'A'
	res_ligand_ID = '216'
	res_ligand_name = 'PRP'
	res_chain = 'A'   ##the chain name that user want to retain
	other_ligands = ['A', '215', 'MG', 'A', '218', 'HOH', 'A', '219', 'HOH'] ##except the reference ligand, other ions or H2O that user want to retaine
	design_ligand_name = 'ABC'
	input_pdb = '1D6N_A68K_G102K_F35L_renumber.pdb'  ##input pdb from protein renumber step
	input_name = input_pdb.split('.pdb')[0].split('/')[-1]
	prep_pdb = input_name+'_prep.pdb'
	prep_name = prep_pdb.split('.pdb')[0]
	cat_ID = '131'
	#sometimes users do not need to define the parameter 'cat_ID', in this study we want to bind our ligand to the special residue 131, so we defne cat_ID = '131'
	#if users do net define this parameter, we also do not need to execute the 'change_pos' function, please comment them out
	main()
