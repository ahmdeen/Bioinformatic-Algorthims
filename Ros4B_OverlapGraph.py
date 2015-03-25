"""
Overlap Graph Problem

Construct the overlap graph of a collection of k-mers.

Given: A collection Patterns of k-mers.

Return: The overlap graph Overlap(Patterns), in the form of an adjacency list.
"""

'''Definitions'''



def OverlapGraph(dna):
	

	checker = lambda pair:pair[0][1:] == pair[1][:-1]
	printer = lambda pair: ' -> '.join(pair)

	#Get all pairs but not inculding itself
	pairs = ([dna1, dna2] for i, dna1 in enumerate (dna) for j,dna2 in enumerate(dna) if i != j)

	overlaps = map(printer, filter(checker, pairs))

	return overlaps

'''Input/Output'''

with open('Data/rosalind_4b.txt') as infile:
	dna = [line.strip() for line in infile.readlines()]

answer = OverlapGraph(dna)

print '\n'.join(answer)

with open('Ros4B_Answer.txt', 'w') as outfile:
	outfile.write('\n'.join(answer))