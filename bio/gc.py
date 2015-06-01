
content = {}
gene = open('rosalind_gc (4).txt','r')
genes = {} 
key = ''
while True:
	line = gene.readline().strip('\n')
	if not line: break
	if '>' in line: 
		key = line.strip('>')
		genes[key]=''
	else : genes[key] += line
for key in genes:
	g = genes[key]
	gc = 0
	for c in g:
		if c in 'G': gc += 1
		elif c in 'C': gc += 1
	content[key]= (gc*1.0/len(g))*100
import operator
print max(content.iteritems(), key=operator.itemgetter(1))[0]
print max(content.iteritems(), key=operator.itemgetter(1))[1]
