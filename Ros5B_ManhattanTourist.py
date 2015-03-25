"""
Length of a Longest Path in the Manhattan Tourist Problem

Find the length of a longest path in a rectangular city.

"""

'''Functions'''

def ManhattanTouristLP(n, m, downMatrix, rightMatrix):
	'''Return: The length of a longest path'''
	#Initialize Path Matrix as a Zero Matrix
	S = [[0]*(m+1) for i in xrange(n+1)]

	for i in xrange(1, n + 1):
		S[i][0] = S[i-1][0] + downMatrix[i-1][0]
	for j in xrange(1, m + 1):
		S[0][j] = S[0][j-1] + rightMatrix[0][j-1]

	for i in xrange(1, n+1):
		for j in xrange(1, m+1):
			S[i][j] = max(S[i-1][j] + downMatrix[i-1][j], S[i][j-1] + rightMatrix[i][j-1])

	return S[n][m]

'''Input/Output'''

with open('Data/rosalind_5b.txt') as inputData:
	n, m = map(int, inputData.readline().strip().split())
	downMatrix, rightMatrix = [[map(int, row.split()) for row in matricies.split('\n')] for matricies in inputData.read().strip().split('\n-\n')]

inputData.close()

answer = str(ManhattanTouristLP(n, m, downMatrix, rightMatrix)) 

print answer

with open('Ros5B_Answer.txt', 'w') as outputData:
	outputData.write(answer)



