# coding=utf-8
import re, sys

#input_pdbfile = '1bzy.pdb'
input_pdbfile = sys.argv[1]
with open(input_pdbfile, 'r') as f:
    data = f.read().split('\n')
f.close()
het = [n for n in data if n.startswith('HETATM')]


def get_chain(chain_lst, ligand_lst):
    reg = '|'.join(chain_lst)
    re_reg = re.compile(reg)
    reg_lig = '(%s)' % '|'.join(ligand_lst)
    re_reg_lig = re.compile(reg_lig)
    het = [n for n in data if n.startswith('HETATM')]
    ligand = [n for n in het if re_reg.match(n.split()[4]) and re_reg_lig.match(n.split()[3])]
    atom = [n for n in data if n.startswith('ATOM')]
    chains = [n for n in atom if re_reg.match(n.split()[4])]
#    chains.extend(ligand)
    file_name = input_pdbfile.split('.')[0]+'_chain'+''.join(chain_lst)+'.pdb'
    with open(file_name, 'w') as w:
        w.write('\n'.join(chains))
        w.write('\nTER\nEND\n')
    w.close()

#get_chain(['A', 'B'], [])
#for example sys.argv[2] = AB
retained_chain = []
for i in sys.argv[2]:
    retained_chain.append(i)
get_chain(retained_chain, [])