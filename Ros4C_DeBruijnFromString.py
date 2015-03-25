"""
De Bruijn Graph from a String Problem

Construct the de Bruijn graph of a string.

Given: An integer k and a string Text.

Return:DeBruijnk(Text), in the form of an adjacency list.
"""

'''Functions'''

def deBruijnFromString(k, Text):

	dbDict = dict()
	for kmer in (Text[i:i+k] for i in xrange(len(Text)-k+1)):
		if kmer[:-1] in dbDict:
			dbDict[kmer[:-1]].add(kmer[1:])
		else:
			dbDict[kmer[:-1]] = {kmer[1:]}

	dbGraph = [' -> '.join([item[0], ','.join(item[1])]) for item in dbDict.items()]
	return dbGraph

'''Input/Output'''

with open('Data/rosalind_4c.txt') as infile:
	k = int(infile.readline().strip())
	dna = infile.readline().strip()

answer = deBruijnFromString(k, dna)
print '\n'.join(answer)

with open('Ros4C_Answer.txt', 'w') as outfile:
	outfile.write('\n'.join(answer))

