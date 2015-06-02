f = open('rosalind_splc.txt','r')
f.readline()
strand = ''
introns = list()
while True:
	line = f.readline().strip('\n')
	if '>' not in line: strand += line
	else: break
intron = ''
while True:
	line = f.readline().strip('\n')
	if not line: 
		introns.append(intron)
		break
	if '>' not in line: intron+= line
	else: 
		introns.append(intron)
		intron = ''
for i in range(len(introns)):
	strand = strand.replace(introns.pop(0),'')
strand = strand.replace('T','U')
codons = {'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG':'L','UCU':'S', 'UCC':"S", 'UCA': 'S', 'UCG':'S', 'UAU':'Y', 'UAC':'Y', 'UAA': '', 'UAG':'','UGU':'C','UGC':'C', 'UGA':'', 'UGG':'W', 'CUU':'L','CUC':'L', 'CUG': 'L', 'CUA':'L', 'CCG':'P','CCA':'P', 'CCU':'P','CCC':'P', 'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q','CGU':'R','CGA':'R','CGC':'R','CGG':'R','AUU':'I','AUA':'I','AUC':'I','AUG':'M','ACU':'T','ACA':'T','ACG':'T','ACC':'T','AAU':'N','AAC':'N','AAA':'K','AAG':'K','AGU':'S', 'AGC':'S', 'AGA':'R','AGG':'R','GUU':'V','GUC':'V','GUA':'V','GUG':'V','GCU':'A','GCC':'A','GCA':'A','GCG':'A','GAU':'D','GAC':'D','GAA':'E','GAG':'E','GGU':'G','GGC':'G','GGA':'G','GGG':'G'}
protein = ''
for i in xrange(0,len(strand),3):
	protein += codons[strand[i:i+3]]
print protein
