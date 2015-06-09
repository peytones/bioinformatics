f = open('rosalind_sseq.txt','r')
f.readline()
strand = ''
while True:
	line = f.readline().strip('\n')
	if '>' in line: break
	strand += line
motif = ''
while True:
	line = f.readline().strip('\n')
	if not line: break
	motif += line
indices = ''
index = 0
for i in range(len(strand)):
	if index<len(motif) and strand[i] in motif[index]:
		index += 1
		indices += str(i+1) + ' '
print indices

