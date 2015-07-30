n = 3
count = 0
f = open('s.txt', 'w')
import itertools
for i,j,k in itertools.product(xrange(n*-1,n+1,1), repeat = n):
	if i != 0 and j!=0 and k!=0:
		p = [abs(i),abs(j),abs(k)]
		if len(p) == len(set(p)):
			s = i,j,k
			f.write((str(s).strip('(').strip(')').replace(',','')) + '\n')
			count += 1
print count

