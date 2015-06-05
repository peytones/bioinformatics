f = open('rosalind_grph.txt','r')
from collections import OrderedDict
strands = OrderedDict()
key = ''
while True:
	line = f.readline().strip('\n')
	if not line: break
	if '>' in line:
		key = line.strip('>')
		strands[key] = ''
	elif '>' not in line: strands[key] += line
for i in range(len(strands)):
	strand = strands.values()[i]
	k = 0
	while True:
		if k == i: k += 1
		if k>=len(strands): break
		if strand[len(strand)-3:] in strands.values()[k][:3]:
			print strands.keys()[i], strands.keys()[k]
			k += 1
		else: k += 1