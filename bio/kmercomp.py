f = open('rosalind_kmer.txt','r')
f.readline()
strand = ''
while True:
	line = f.readline().strip('\n')
	if not line: break
	strand += line
from collections import OrderedDict
kmers = OrderedDict()
from itertools import product
for x in product('ACGT',repeat=4):
	x = str(x).strip('()').strip('\'').replace(',','').replace(' ','').replace('\'','')
	kmers[x]=0
for i in range(len(kmers)):
	st = kmers.keys()[i]
	for j in range(len(strand)-3):
		if strand[j:j+4] in st: 
			kmers[st] += 1
print str(kmers.values()).strip('()').strip('[]').replace(',','')