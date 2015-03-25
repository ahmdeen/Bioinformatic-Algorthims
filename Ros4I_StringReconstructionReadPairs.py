"""
String Reconstruction from Read-Pairs Problem

Reconstruct a string from its paired composition.

Given: Integers k and d followed by a collection of paired k-mers PairedReads.

Return: A string Text with (k, d)-mer composition equal to PairedReads. 
(If multiple answers exist, you may return any one.)
"""

from Ros4F_EulerianPath import EulerianPath


'''Functions'''

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
	k, d = map(int, infile.readline().strip().split())
	pairedReads = [line.strip().split('|') for line in infile.readlines()]

answer = StringReconstructionReadPairs(k, d, pairedReads)

print answer

with open('Ros4I_Answer.txt', 'w') as outfile:
	outfile.write(answer)
