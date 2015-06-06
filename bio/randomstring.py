f = open('rosalind_prob.txt', 'r')
dna = f.readline().strip('\n')
freq = map(float, f.readline().strip('\n').split(' '))
gc = (dna.count('G') + dna.count('C'))
newfreq = []
import math
for i in range(len(freq)):
	print i
	newfreq.append((math.log10(freq[i]/2)*gc) + (math.log10((1-freq[i])/2)*(len(dna)-gc)))
print str(newfreq).strip('[]').replace(',', ' ')

