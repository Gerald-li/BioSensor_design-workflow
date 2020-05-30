# coding=utf-8
import os, re, sys

def get_mutations(pdb1,pdb2):
	inf_wild = open(pdb1, 'r')
	inf_mut = open(pdb2, 'r')
	lines_wild = inf_wild.readlines()
	inf_wild.close()
	res_info_wild = []
	lines_mut = inf_mut.readlines()
	inf_mut.close()
	res_info_mut = []
	for line in lines_wild:
		if line.startswith(('ATOM', 'ANISOU')):
			resname = line[17:20].strip()
			res_id = line[22:27].strip()
			res_chain = line[21:22].strip()
			if res_chain + '-' + res_id + '_' + resname not in res_info_wild:
				res_info_wild.append(res_chain + '-' + res_id + '_' + resname)
			else:
				continue
	for line in lines_mut:
		if line.startswith(('ATOM', 'ANISOU')):
			resname = line[17:20].strip()
			res_id = line[22:27].strip()
			res_chain = line[21:22].strip()
			if res_chain + '-' + res_id + '_' + resname not in res_info_mut:
				res_info_mut.append(res_chain + '-' + res_id + '_' + resname)
			else:
				continue
	dif_mut = list(set(res_info_mut).difference(set(res_info_wild)))
	#l.sort(key=lambda d:int(d))
	new_mut = sorted(dif_mut,key = lambda i:int(re.match(r'\w-(\d+)',i).group(1)))
	dif_wild = list(set(res_info_wild).difference(set(res_info_mut)))
	new_wild = sorted(dif_wild,key = lambda i:int(re.match(r'\w-(\d+)',i).group(1)))
	outfi = open(pdb2.split('.pdb')[0] + '.csv','w')
	outfi.write(str(len(new_mut)) + ' mutations\nwild residues\tmutanted residues\n')
	for i in range(len(new_wild)):
		outfi.write(new_wild[i] + '\t' + new_mut[i].split('_')[-1] + '\n')
	outfi.close()

if __name__ == '__main__':
	#attentions
	#
	# we need a wild type pdb structure as a reference
	# pdb1 = sys.argv[1]
	pdb1 = '../1.2/1D6N_A68K_G102K_F35L_renumber.pdb'
	#pdb2 = sys.argv[2]
	designed_pdb_path = '../2.2/'  #the result files will be stroed in this directroy
	dirs = os.listdir(designed_pdb_path)
	pdb2 = []
	for fi in dirs:
		if fi.startswith('UM') and fi.split('_')[-2] == 'DE':
			pdb2.append(designed_pdb_path + fi)
	for i in pdb2:
		get_mutations(pdb1, i)

	#print '--==--Finish--==--'