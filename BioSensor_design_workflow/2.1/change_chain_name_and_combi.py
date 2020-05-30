import sys,os

alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]

def get_chain_info():
	chains=[]
	input_pdbfile = sys.argv[1]
	with open(input_pdbfile, 'r') as f:
		lines = f.readlines()
	f.close()
	for line in lines:
		if line.startswith(('ATOM', 'HETATM', 'TER', 'ANISOU')):
			chain_info = line[21:22]
			chains.append(chain_info)
#			print chains
	A = list(set(alphabet).difference(set(chains)))
#	print sorted(A)
	return sorted(A)
			
def change_chain_info(pdbfile):
	with open(pdbfile, 'r') as f:
		lines = f.readlines()
	f.close()
	ex_alp = get_chain_info()
	print(ex_alp)
	change_chain_name = ex_alp[0]
#	print change_chain_name
#	outfi = open(pdbfile,'w')
	change_pdb = ''
	for line in lines:		
		if line.startswith(('ATOM', 'HETATM', 'ANISOU')):
			l = list(line)
			l[21] = change_chain_name
			newS = ''.join(l)
			change_pdb = change_pdb + newS
#			outfi.write(newS)
		elif line.startswith('END'):
			line = ''
			change_pdb = change_pdb + line
#			outfi.write(line)
		else:
			change_pdb = change_pdb + line
#			outfi.write(line)
#			chains.append(chain_info)
	change_pdb = change_pdb + 'END'
	return change_pdb
#	print change_pdb	
#	outfi.write('END')
#	outfi.close()

def combi_pdb(combi_file_name):

	input_pdbfile = sys.argv[1]
	with open(input_pdbfile, 'r') as f:
		lines = f.readlines()
	f.close()
	add_pdb = change_chain_info(sys.argv[2])
	output_pdb = open(combi_file_name,'w')
	for line in lines:
		if line.startswith('END'):
			line = ''
			output_pdb.write(str(line))
		else:
			output_pdb.write(str(line))
#	add_pdb = change_chain_info('1gm9_prep_chainB_1568_CA.pdb',1)

#	print add_pdb
	output_pdb.write(add_pdb)
	output_pdb.close()
	
	
	
			
			
#print get_chain_info()


#combi_pdb(sys.argv[1].split('.pdb')[0]+sys.argv[2].split('prep')[-1])
combi_pdb('combi_ligands.pdb')
