f = open('rosalind_pmch.txt','r')
f.readline()
strand = f.readline().strip('\n')
au = strand.count('A')
gc = strand.count('G')
from math import factorial
print  long(factorial(au)) * long(factorial(gc))
