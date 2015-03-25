"""
Longest Common Subsequence Problem

Given: Two strings.

Return: A longest common subsequence of these strings.

"""

'''Functions'''

def longestCommonSubsequence(seq1, seq2):
	'''Return a longest common subsequence of the input strings'''
	lenSeq1 = len(seq1)
	lenSeq2 = len(seq2)

	S = [[0]*(lenSeq2+1) for k in xrange(lenSeq1 + 1)]

	for i in xrange(lenSeq1):
		for j in xrange(lenSeq2):

			if seq1[i] == seq2[j]:
				S[i+1][j+1] = S[i][j]+1
			else:
				S[i+1][j+1] = max(S[i+1][j], S[i][j+1])


	longestSubSeq = ''

	a = len(seq1)
	b = len(seq2)
	while a*b != 0:
		if S[a][b] == S[a-1][b]:
			a -= 1
		elif S[a][b] == S[a][b - 1]:
			b -= 1
		else:
			longestSubSeq = seq1[a-1] + longestSubSeq
			a -= 1
			b -= 1

	return longestSubSeq


'''Input/Output'''

with open('Data/rosalind_5c.txt') as inputData:
	seq1, seq2 = [line.strip() for line in inputData.readlines()] 

inputData.close()

answer = longestCommonSubsequence(seq1, seq2)
print answer

with open('Ros5C_Answer', 'w') as outputData:
	outputData.write(answer)
