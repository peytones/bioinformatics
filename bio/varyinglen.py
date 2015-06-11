strand = 'NQBOWLKVECAM'
f = open('file.txt', 'r+')
length = len(strand)
for i in range(length):
	f.write(str(strand[i]+'\n').strip(' '))
	for k in range(length):
		f.write(str(strand[i]+strand[k]+'\n').strip(' '))
		for j in range(length):
			f.write(str(strand[i]+strand[k]+strand[j]+'\n').strip(' '))
			for l in range(length):
				f.write(str(strand[i]+strand[k]+strand[j]+strand[l]+'\n').strip(' '))

#Better solution to come so the for loops and length of strings are not hard coded.
