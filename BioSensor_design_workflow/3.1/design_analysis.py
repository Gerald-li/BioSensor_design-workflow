import os

def design_score(ligand_name, path):
	dirs = os.listdir(path)
	outfi = open('design_'+ligand_name+'.out','w')
	count = 0
	for fi in dirs:
		if fi.startswith('UM') and fi.split('_')[-1] == 'DE.out':
			count += 1
			infi = open(path + fi, 'r')
			lines = infi.readlines()
			line_1 = lines[0]
			line_2 = lines[1:]
			if count == 1:
				for line in lines:
					outfi.write(line)
			if count > 1:
				for line in line_2:
					outfi.write(line)
			infi.close()
	outfi.close()
	return outfi
		
def design_filter(filter_condition):
	des_fil = open('design_'+ligand_name+'.filter','w')		
	des_fil.write(filter_condition)
	des_fil.close()
	return des_fil

if __name__ == '__main__':
	design_out_file_dir = '../2.2/'
	#attentions
	#more filter_condition information see ROSETTA software about enzymedesign filter condition
	filter_condition = '''
req all_cst value < 10.0
req SR_2_interf_E_1_2 value < -5.0
output sortmin total_score
'''
	ligand_name = 'ABC'   ##user defined
	#design_score(ligand_name, path)
	#design_filter(filter_condition)
	##ROSETTA software also provide a perl scritp to analysis the designed out file, more information see ROSETTA software about 'DesignSelect.pl'
	analysis_command = 'perl $ROSETTA_HOME/src/apps/public/enzdes/DesignSelect.pl -d ' + design_score(ligand_name, design_out_file_dir).name + ' -c ' + design_filter(filter_condition).name + ' -tag_column last > filtered_designs_' + ligand_name + '.out'
	#in the "filtered_designs_'ligand_name'.out" file we can get the out information that match the filter criteria.
	os.system(analysis_command)
