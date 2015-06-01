import itertools
a = ['IQH','IQG','IQC','IQM','QHG','QHC','QHM','HGC','HGM','GCM']
for i in range(len(a)):
	k = list(itertools.permutations(a[i]))
	for n in range(len(k)):
		print str(k[n]).strip('()').replace(',', '').replace('\'', '')