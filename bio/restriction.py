orig = 'TCAATGCATGCGGGTCTATATGCAT'
comp = orig.replace('A', 't').replace('T', 'a').replace('G','c').replace('C','g').upper()
for i in xrange(0,len(orig)-4,1):
	for k in xrange(i+3,len(orig),1):
		print orig[i:k], comp[-k:-i+1]
		if orig[i:k] in comp[-k:-i+1]:
			print i, k-i
print orig
print comp