"""
Implement GreedySorting

Given: A signed permutation P.

Return: The sequence of permutations corresponding to applying GreedySorting to P, ending with the identity permutation.
"""

from operator import neg

'''Functions'''

#Where P is the permutation
def GreedySorting(P):

	permSeq = []

	kInd = lambda p, k: map(abs, p).index(k)

	kSort = lambda p, i, j: p[:i] + map(neg, p[i:j+1][::-1]) + p[j+1:]

	i = 0
	while i < len(P):
		if P[i] == i+1:
			i += 1 
		else:
			P = kSort(P, i, kInd(P, i+1))
			permSeq.append(P)

	return permSeq

'''Input/Output'''

with open('Data/rosalind_6a.txt') as infile:
	p = map(int, infile.read().strip().lstrip('(').rstrip(')').split())

revList = GreedySorting(p)

revList = ['('+' '.join([['', '+'][element > 0] + str(element) for element in permutation])+')' for permutation in revList]

print '\n'.join(revList)

with open('Ros6A_Answer.txt', 'w') as outfile:
	outfile.write('\n'.join(revList))

