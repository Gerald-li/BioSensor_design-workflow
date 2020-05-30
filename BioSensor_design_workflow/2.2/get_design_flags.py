import os, sys

def get_design_flags(ligand_name):
	command = "sed -e 's/res_ligand_params_file/design_"+ligand_name+".params/g' -e 's/enz_score.out/enz_score_"+ligand_name+".out/g' design.flags > design_out.flags"
	os.system(command)

if __name__ == '__main__':
	ligand_name = "ABC"
	get_design_flags(ligand_name)
