f = open('rosalind_cons.txt','r')
dna = []
f.readline()
strand = ''
while True:
	line =f.readline().strip('\n')
	if not line: 
		dna.append(strand)
		break
	if '>' in line: 
		dna.append(strand)
		strand = ''
	elif '>' not in line: strand += line
a = {}
c = {}
t = {}
g = {}
for i in range(len(dna[0])):
	a[i] = 0
	c[i] = 0
	t[i] = 0
	g[i] = 0
for i in range(len(dna)):
	strand = dna[i]
	for k in range(len(strand)):
		if strand[k] == 'A': a[k] += 1
		elif strand[k] == 'T': t[k] += 1
		elif strand[k] == 'G': g[k] += 1
		elif strand[k] == 'C': c[k] += 1
consensus = ''
for i in range(len(dna[0])):
	aval = a.values()[i]
	cval = c.values()[i]
	tval = t.values()[i]
	gval = g.values()[i]
	maximum = max(aval,tval,gval,cval)
	if maximum == aval: consensus += 'A'
	elif maximum == tval: consensus += 'T'
	elif maximum == cval: consensus += 'C'
	elif maximum == gval: consensus += 'G'
print consensus
print 'A: ' + str(a.values()).strip('[]').replace(',', ' ')
print 'C: ' + str(c.values()).strip('[]').replace(',', ' ')
print 'G: ' + str(g.values()).strip('[]').replace(',', ' ')
print 'T: ' + str(t.values()).strip('[]').replace(',', ' ')
