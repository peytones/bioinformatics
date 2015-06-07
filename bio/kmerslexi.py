f = open('kmer.txt','r')
symbols = f.readline().strip('\n').replace(' ', '')
length = int(f.readline().strip('\n'))
for i in range(len(symbols)):
	for k in range(len(symbols)):
		print symbols[i]+symbols[k:k+length-1]
