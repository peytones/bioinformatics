f = open('rosalind_lexf.txt','r')
symbols = f.readline().strip('\n').replace(' ', '')
length = int(f.readline().strip('\n'))
for i in range(len(symbols)):
	for k in range(len(symbols)):
		for j in range(len(symbols)):
			for l in range(len(symbols)):
				length += 0

#much better solution. product acts as nested for loop that I created by hand in my solution
from itertools import product
print '\n'.join([''.join(x) for x in product(symbols,repeat=length)])