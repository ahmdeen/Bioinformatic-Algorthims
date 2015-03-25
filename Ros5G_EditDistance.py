"""
Edit Distance Problem

Find the edit distance between two strings.

Given: Two protein strings.

Return: The edit distance between these strings.

"""


'''Functions'''

def editDist(seq1, seq2):
	'''Returns the Edit Distance between the two input strings'''

	len1, len2 = len(seq1), len(seq2)

	#Initialize Matrix

	M = [[0 for j in xrange(len2 + 1)] for i in xrange(len1+1)]
	
	#Fill out the first row and the first column of the Matrix
	for i in range(1, len1 + 1):
		M[i][0] = i 
	for j in range(1, len2 + 1):
		M[0][j] = j

	#Fill out the rest of the Matrix

	for i in xrange(1, len1 + 1):
		for j in xrange (1, len2 + 1):
			if seq1[i-1] == seq2[j-1]:
				M[i][j] = M[i-1][j-1]
			else:
				M[i][j] = min(M[i-1][j] +1, M[i][j-1] + 1, M[i-1][j-1] + 1)

	return M[len1][len2]

'''Input/Output'''

with open('Data/rosalind_5g.txt') as infile:
	seq1, seq2 = [line.strip() for line in infile.readlines()]

answer = editDist(seq1, seq2)
print str(answer)

with open('Ros5G_Answer.txt', 'w') as outfile:
	outfile.write(str(answer))



