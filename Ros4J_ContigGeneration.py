"""
Contig Generation Problem

Generate the contigs from a collection of reads (with imperfect coverage).

Given: A collection of k-mers Patterns.

Return: All contigs in DeBruijn(Patterns). (You may return the strings in any order.)
"""

from compiler.ast import flatten

'''Functions'''

def contigGenerate(kmers):
	edges = {}
	for kmer in kmers:
		if kmer[:-1] in edges:
			edges[kmer[:-1]].append(kmer[1:])
		else:
			edges[kmer[:-1]] = [kmer[1:]]

	balEdges = []
	nonBalEdges = []

	outVals = reduce(lambda a,b:a+b, edges.values())
	for node in set(outVals+edges.keys()):
		outVal = outVals.count(node)
		if node in edges:
			inVal = len(edges[node])
		else:
			inVal = 0

		if inVal == outVal == 1:
			balEdges.append(node)
		else:
			nonBalEdges.append(node)

	
	#lambda function to get the contigs
	genContigs = lambda x,y: flatten([y+edge[-1] if edge not in balEdges else genContigs(edge,y+edge[-1]) for edge in edges[x]])
	

	contigs = sorted(flatten([genContigs(source, source) for source in set(nonBalEdges) & set(edges.keys())]))

	return contigs

'''Input/Output'''

with open('Data/rosalind_4j.txt') as infile:
	patterns = [line.strip() for line in infile.readlines()]

answer = contigGenerate(patterns)

print '\n'.join(answer)

with open('Ros4j_Answer.txt', 'w') as outfile:
	outfile.write('\n'.join(answer))

