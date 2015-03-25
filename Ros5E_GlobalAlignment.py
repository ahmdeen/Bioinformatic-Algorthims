"""

Global Alignment Problem

Find the highest-scoring alignment between two strings using a scoring matrix.
Given: Two protein strings.

Return: The maximum alignment score of these strings followed by an 
alignment achieving this maximum score. 
"""
import os

'''Classes'''
class blosum62(object):
	'''Class to score proteins using the BLOSUM62 matrix'''

	def __init__(self):
		'''Initalize BLOSUM62 Matrix'''
		with open(os.path.join(os.path.dirname(__file__), 'DATA/BLOSUM62.txt')) as inFile:
			lines = [line.strip().split() for line in inFile.readlines()]
			self.S = {(item[0], item[1]): int(item[2]) for item in lines} 

	def __getitem__(self, pair):
		'''Returns the score of a given pair'''
		return self.S[pair[0],pair[1]]

'''Functions'''
def globalAlignment(seq1, seq2, ScoreMatrix, sig):
	'''Returns the global alignment of the input sequences utilizing the given ScoringMatrix and indel penalty'''
	len1, len2 = len(seq1), len(seq2)

	S = [[0]*(len2+1) for s in xrange(len1+1)]
	backtrack = [[0]*(len2+1) for bt in xrange(len1+1)]

	for i in xrange(1, len1+1):
		S[i][0] = -i*sig
	for j in xrange(1, len2+1):
		S[0][j] = -j*sig

	for i in xrange(1, len1+1):
		for j in xrange(1, len2+1):
			scoreList  = [S[i-1][j] - sig, S[i][j-1] - sig, S[i-1][j-1] + ScoreMatrix[seq1[i-1], seq2[j-1]]]
			S[i][j] = max(scoreList)
			backtrack[i][j] = scoreList.index(S[i][j])
	#-----	
	indelInsertFcn = lambda seq, i: seq[:i] + '-' + seq[i:]
	#-----
	align1, align2 = seq1, seq2
	a, b = len1, len2
	maxScore = str(S[a][b])

	while a*b != 0:
		if backtrack[a][b] == 0:
			a -= 1
			align2 = indelInsertFcn(align2, b)
		elif backtrack[a][b] == 1:
			b -= 1
			align1 = indelInsertFcn(align1, a)
		else:
			a -= 1
			b -= 1


	for i in xrange(a):
		align2 = indelInsertFcn(align2, 0)
	for j in xrange(b):
		align1 = indelInsertFcn(align1, 0)

	return maxScore, align1, align2


'''Input/Output'''
"""
seq1 = 'PLEASANTLY'
seq2 = 'MEANLY'
"""
with open('Data/rosalind_5e.txt') as infile:
	seq1, seq2 = [line.strip() for line in infile.readlines()]

indelPenalty = 5
alignment = globalAlignment(seq1,seq2, blosum62(), indelPenalty)

answer = '\n'.join(alignment)
print answer

with open('Ros5E_Answer.txt', 'w') as outfile:
	outfile.write(answer)



