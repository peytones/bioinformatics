f = open('rosalind_iev.txt','r')
probabilites = {1:1, 2:1, 3:1, 4:.75, 5:.5, 6:0}
parents = [int(x) for x in f.readline().split()]
offspring = 0
for i in xrange(1,6,1):
	offspring += int(parents[i])*probabilites[i]*2
print offspring