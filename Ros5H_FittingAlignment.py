"""

Fitting Alignment Problem

Construct a highest-scoring fitting alignment between two strings.

Given: Two DNA strings v and w, where v has length at most 10000 and w has length at most 1000.

Return: The maximum score of a fitting alignment of v and w, followed by a fitting alignment 
achieving this maximum score. Use the simple scoring method in which matches count +1 and both the 
mismatch and indel penalties are equal to 1. (If multiple fitting alignments achieving the maximum 
score exist, you may return any one.)

"""

'''Functions'''

def fitAlignment(seq1, seq2):
	'''Returns the maximum score of a fitting alignment of the input sequences, followed by the alignment'''


	len1, len2 = len(seq1), len(seq2)
	#Initialize Score and Backtrack Matricies as 0 matricies

	S = [[0 for j in xrange(len2 + 1)] for i in xrange(len1 + 1)]
	backtrack = [[0 for j in xrange(len2 + 1)] for i in xrange(len1 + 1)]

	#Complete the entries in the matricies
	for i in xrange(1, len1 + 1):
		for j in xrange(1, len2 + 1):
			scoreList = [S[i-1][j] - 1, S[i][j-1] - 1, S[i-1][j-1] + [-1, 1][seq1[i-1] == seq2[j-1]]] #*
			S[i][j] = max(scoreList)
			backtrack[i][j] = scoreList.index(S[i][j])

	#Get the score of the end alignment of seq2, the shorter sequence

	b = len2
	a = max(enumerate([S[row][b] for row in xrange(len2, len1)]), key = lambda y:y[1])[0] + len2
	maxScore = str(S[a][b])

	#The initial alignment of seq1 to seq2
	align1, align2 = seq1[:a], seq2[:b]

	#-----
	insertIndelFcn = lambda seq, i: seq[:i] + '-' + seq[i:]
	#-----

	#Backtrack to find fitting alignment

	while a*b != 0:
		if backtrack[a][b] == 0:
			a -= 1
			align2 = insertIndelFcn(align2, b)
		elif backtrack[a][b] == 1:
			b -= 1
			align1 = insertIndelFcn(align1, a)
		elif backtrack[a][b] == 2:
			a -= 1
			b -= 1

	# Need to cut off seq1 at the ending point
	align1 = align1[a:]

	return maxScore, align1, align2


'''Input/Output'''

with open('Data/rosalind_5h.txt') as infile:
	seq1, seq2 = [line.strip() for line in infile.readlines()]

answer = fitAlignment(seq1, seq2)
print '\n'.join(answer)

with open('Ros5H_Answer.txt', 'w') as outfile:
	outfile.write('\n'.join(answer))