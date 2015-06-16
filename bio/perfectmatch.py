f = open('rosalind_pmch.txt','r')
f.readline()
strand = ''
while True:
	line = f.readline().strip('\n')
	if not line: break
	strand += line
au = strand.count('A')
gc = strand.count('G')
from math import factorial
print au, gc
print factorial(au) * factorial(gc)