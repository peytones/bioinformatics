s = 'AACGGACTTAGGGACTTAGATGGACTTAGACGGACTTAGGACTTAAGGACTTAATGCGGACTTAGGACTTAGTTAGTTGGACTTATGGACTTAGGACTTAGGACTTAATCCTGGGACTTACCGGACTTAACGTGGACTTAAGGACTTATGGGGACTTAAGGACTTAACGGGACTTACGGACTTAGTGAGGGACTTAGGACTTACCAGGACTTAGGAAGGACTTATGGACTTATTGCACCGGACTTATTGTAGGGACTTATGGACTTAGGCTAACGTTTCTTGGGCAGGACTTAACAGCGGACTTATTGTCAGGACTTACCAGACAGGACTTATGGACTTAGGACTTAAGGACTTAGTAGGACTTACCGAGAAAGGACTTAGTGGGACTTACGGACTTAGGGACTTAGGACTTAAGGACTTATGTTCCGAATATCTCGGAGGGACTTAGGACTTAGGGACTTAGCCGGACTTAGGACTTAGGACTTAGGACTTATACGGACTTAAATGGACTTAGGACTTAGGACTTAGGTGGGACTTACCAAGGGGGACTTAGGACTTATGGACTTAACGGACTTAACAGAGGACTTAGGGGACTTAGGACTTAACCGCAAGGGACTTATAATGTGGGACTTAGCTGGGGACTTAGGACTTAGGACTTAGAGGACTTAGCTTAGGACTTATGATATAAGGGACTTAGATGGGGACTTAGTCGGACTTACCAGGACTTAGGACTTACGTTAGGACTTAGGACTTAGGACTTAGAGGACTTATTTCATCTACCGGATGGACTTATTAAGGACTTACGGACTTAGGGACTTACTTTTCATGGACTTACGGACTTAGGACTTAGGACTTAGACGGACTTAAGGGACTTACTCAGGACTTAGGACTTAGCAGTCTGGACTTAGGACTTAACCATGGACTTAGGACTTA'
t = 'GGACTTAGGcd '
l = []
for i in range(len(s)):
	for k in range(len(s)):
		if s[i:k] == t:
			l.append(i+1)
print str(l).strip('[]').replace(',', '')