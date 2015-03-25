"""
Overlap Alignment Problem

Construct a highest-scoring overlap alignment between two strings.

Given: Two protein strings s and t, each of length at most 1000.

Return: The score of an optimal overlap alignment of v and w, followed by an alignment 

"""

'''Functions'''

def overlapAlignment(seq1, seq2):
	'''Returns the score of the overlapAlignment as well as the alignment of the two input sequences'''

	len1, len2 = len(seq1), len(seq2)

	#Initialize Score and backtrack matricies
	S = [[0 for j in xrange(len2 + 1)] for i in xrange(len1 + 1)]
	backtrack = [[0 for j in xrange(len2 + 1)] for i in xrange(len1 +1)]

	#Inital Max Score**

	maxScore = -3*(len1 + len2)

	#Complete the Score and backtrack matricies

	for i in xrange(1, len1 + 1):
		for j in xrange(1, len2 + 1):
			#Match = 1, Mismatch/Indel = -2

			scoreList = [S[i-1][j-1] + [-2, 1][seq1[i-1] == seq2[j-1]], S[i-1][j] - 2, S[i][j-1] - 2]
			S[i][j] = max(scoreList)
			backtrack[i][j] = scoreList.index(S[i][j])

			#Check for maximums along final row/column
			if i == len1 or j == len2:
				if S[i][j] > maxScore:
					maxScore = S[i][j]
					maxIndex = (i,j)
	
	a, b = maxIndex
	align1, align2 = seq1[:a], seq2[:b]

	#------------
	insertIndelFcn = lambda seq, i:seq[:i] + '-' + seq[i:]

	#Backtrack to find Alignment

	while a*b != 0:
		if backtrack[a][b] == 1:
			a -= 1
			align2 = insertIndelFcn(align2, b)
		elif backtrack[a][b] == 2:
			b -= 1
			align1 = insertIndelFcn(align1, a)
		else:
			a -= 1
			b -= 1

	align1 = align1[a:]
	align2 = align2[b:] 

	return str(maxScore), align1, align2

'''Input/Output'''

with open ('Data/rosalind_5i.txt') as infile:
	seq1, seq2 = [line.strip() for line in infile.readlines()]

answer = overlapAlignment(seq1, seq2)

print '\n'.join(answer)

with open('Ros5i_Answer.txt', 'w') as outfile:
	outfile.write('\n'.join(answer))




