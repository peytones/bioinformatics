import itertools
perm = list(itertools.permutations([1,2,3,4,5,6]))
print len(perm)
for i in range(len(perm)):
	print str(perm[i]).strip('() , ').replace(',', '')