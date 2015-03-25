"""
String Reconstruction Problem

Reconstruct a string from its k-mer composition.

Given: An integer k followed by a list of k-mers Patterns.

Return: A string Text with k-mer composition equal to Patterns. (If multiple answers exist, you may return 
any one.)
"""

'''Functions'''

"""
String Reconstruction Problem

Given: The adjacency list of a directed graph that has an Eulerian path.

Return: An Eulerian path in this graph.


"""

def StringReconstructionReadPairs(k, d, pairedReads):

	#Dictionary of Edges created from the Paired Reads
	pairDict = dict()
	for pair in pairedReads:
		if (pair[0][:-1],pair[1][:-1]) in pairDict:
			pairDict[(pair[0][:-1],pair[1][:-1])].append((pair[0][1:],pair[1][1:]))
		else:
			pairDict[(pair[0][:-1],pair[1][:-1])] = [(pair[0][1:],pair[1][1:])]

	#Constuct Eulerian Path from the Paired Edges
	pairReadPath = EulerianPath(pairDict)

	string = [pairReadPath[0][i] + ''.join(map(lambda x: x[i][-1], pairReadPath[1:])) for i in xrange(2)]
	Text = string[0][:k+d]+string[1]

	return Text

'''Input/Output'''

with open('Data/rosalind_4i.txt') as infile:
	k = int(infile.readline().strip())
	patterns = [line.strip().split() for line in infile.readlines()]
	d = 0
answer = StringReconstructionReadPairs(k, d, pairedReads)

print answer

with open('Ros4I_Answer.txt', 'w') as outfile:
	outfile.write(answer)