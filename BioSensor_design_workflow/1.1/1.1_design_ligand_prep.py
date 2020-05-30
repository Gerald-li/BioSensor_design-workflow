import os, sys
def get_conf(name,dir_path):
	os.system('mol2convert -imol2 '+name+'.mol2'+' -omae '+name+'.mae')
	os.system('ligprep -g -s 1 -imae '+name+'.mae -omae '+name+'_ligprep.mae')
	while True:
		if os.path.exists(os.path.join(dir_path, name+'_ligprep.mae')):
			break
	os.system('confgenx -m 100 -no_cleanup '+name+'_ligprep.mae')
	while True:
		if os.path.exists(os.path.join(dir_path, name+'_ligprep-out.maegz')):
			break
	os.system('mol2convert -imae '+name+'_ligprep-out.maegz -omol2 '+name+'_ligprep-out_conf.mol2')
def get_params(res_ligand_name,ligand_name):
	## molfile_to_params.py may in different directory in different ROSETTA version (this version is 3.10)
	os.system('$ROSETTA_HOME/scripts/python/public/molfile_to_params.py -n '+res_ligand_name+' -p '+ligand_name+' '+ligand_name+'_ligprep-out_conf.mol2')
	os.system('cat '+ligand_name+'_????.pdb > '+res_ligand_name+'_confs.pdb')
	os.system('rm '+ligand_name+'_????.pdb')
	os.system('cp ' + ligand_name + '.params ' + res_ligand_name + '.params')
	os.system('echo "PDB_ROTAMERS '+res_ligand_name+'_confs.pdb" >> '+res_ligand_name+'.params')


def main():
	input_ligand = sys.argv[1]  ##there need a parameter which is the ligand structure in mol2 type.
	ligand_path = './'
	ligand_name = input_ligand.split('.mol2')[0].split('/')[-1]
	# print(ligand_name)
	get_conf(ligand_name,ligand_path)
	res_ligand_name = 'ABC'     ##rename the ligand to 'ABC', so we can easily record
	get_params(res_ligand_name,ligand_name)

main()
