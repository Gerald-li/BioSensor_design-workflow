import os, sys
def div_list(ls,n):  
	result = []  
	cut = int(len(ls)/n)  
	if cut == 0:  
		ls = [[x] for x in ls]  
		none_array = [[] for i in range(0, n-len(ls))]  
		return ls+none_array  
	for i in range(0, n-1):  
		result.append(ls[cut*i:cut*(1+i)])  
	result.append(ls[cut*(n-1):len(ls)])
	print(result)
	return result

def match_pdb():
	path = './'
	dirs = os.listdir(path)
	match_pdb = []
	for fi in dirs:
		if fi.startswith('UM') and fi.split('_')[-2] == 'match':
			match_pdb.append(fi)
	return match_pdb
	

def design_command(n):
	if len(match_pdb()) < n:
		n = 1
	match_result = div_list(match_pdb(), n)
	for i in range(n):
		fi = open('CPU_' + str(i) + '.sh', 'w')
		for j in match_result[i]:
			fi.write('#!/usr/bin/env bash\n')
			fi.write('$ROSETTA_HOME/bin/enzyme_design.linuxgccrelease @design_out.flags -database $ROSETTA_DATABASE -s '+ j + ' -out:file:o '+j+'_DE.out'+' > ' + j +'_design.log')
			fi.write('\n')
		fi.close()
		os.system('sh ' + 'CPU_' + str(i) + '.sh&')

if __name__ == '__main__':
	design_command(2)  ##users can define how many CPU sources can be used based on match result