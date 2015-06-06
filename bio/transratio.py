f = open('rosalind_tran.txt','r')
f.readline()
strand1 = ''
while True:
	line = f.readline().strip('\n')
	if '>' in line: break
	elif '>' not in line: strand1 += line
strand2 = ''
while True:
	line = f.readline().strip('\n')
	if not line: break
	strand2 += line
transition = 0
transversion = 0
pyrimidine = 'CT'
purine = 'AG'
for i in range(len(strand1)):
	if strand1[i] not in strand2[i]:
		if (strand1[i] in purine and strand2[i] in purine) or (strand1[i] in pyrimidine and strand2[i] in pyrimidine): 
			transition += 1
		elif (strand1[i] in purine and strand2[i] in pyrimidine) or (strand1[i] in pyrimidine and strand2[i] in purine): 
			transversion += 1
print transition*1.0/transversion