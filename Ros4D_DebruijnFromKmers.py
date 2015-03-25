"""
De Bruijn Graph from k-mers Problem

Construct the de Bruijn graph from a collection of k-mers.

Given: A collection of k-mers Patterns.

Return: The de Bruijn graph DeBruijn(Patterns), in the form of an adjacency list.
"""


'''Functions'''
def deBruijnFromKmers(kmers):
	dbDict = dict()
	i = 0
	for kmer in kmers:
		#print kmer
		
		if kmer[:-1] in dbDict:
			dbDict[kmer[:-1]].append(kmer[1:])
			dbDict[kmer[:-1]].sort()
			
		else:
			dbDict[kmer[:-1]] = [kmer[1:]]
			#print 1, i, kmer, kmer[:-1], kmer[1:]
			#i += 1
	#print dbDict
	dbGraph = [' -> '.join([item[0], ','.join(item[1])]) for item in dbDict.items()]
	return dbGraph

'''Input/Output'''


with open('Data/rosalind_4d.txt') as infile:
	kmers = [line.strip() for line in infile.readlines()]

#kmers = ['GAGG', 'CAGG', 'GGGG', 'GGGA', 'CAGG', 'AGGG', 'GGAG']

answer = sorted(deBruijnFromKmers(kmers))

print '\n'.join(answer)

with open('Ros4D_Answer', 'w') as outfile:
	outfile.write('\n'.join(answer))
	
