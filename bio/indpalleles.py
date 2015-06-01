k = 2
n = 1
prob = 0
for i in xrange(1,k+1,1):
	prob += 1.0/(4 ** (i)) *  (2 ** i)
print prob