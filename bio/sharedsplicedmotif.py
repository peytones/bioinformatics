stranda = ''
strandb = ''
f = open('rosalind_lcsq.txt','r')
f.readline()
while True:
	line = f.readline().strip('\n')
	if not '>' in line: stranda += line
	else: break
while True:
	line = f.readline().strip('\n')
	if not line: break
	strandb += line
print strandb
motif = '' 
index = 0
for i in range(len(stranda)):
	dna = stranda[i]
	if dna in strandb: 
		motif += dna
		index = strandb.find(dna) + 1
		strandb = strandb[index:]
print motif