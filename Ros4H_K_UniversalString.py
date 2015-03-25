"""
k-Universal Circular String Problem

Find a k-universal circular binary string.

Given: An integer k.

Return: A k-universal circular string. (If multiple answers exist, you may return any one.)
"""


from Ros4E_EulerianCycle import eulerian_cycle
from itertools import product

'''Functions'''

def k_UniversalString(k):

	uDict = dict()
	for kmer in [''.join(item) for item in product('01', repeat=k)]:
		if kmer[:-1] in uDict:
			uDict[kmer[:-1]].append(kmer[1:])
		else:
			uDict[kmer[:-1]] = [kmer[1:]]

	path = eulerian_cycle(uDict)

	return path


'''Input/Output'''
with open('Data/rosalind_4h.txt') as infile:
	k = int(infile.readline().strip())

answer = k_UniversalString(k)

print ''.join([item[0] for item in answer[:-1]])

with open('Ros4H_Answer.txt', 'w') as outfile:
	outfile.write(''.join([item[0] for item in answer[:-1]]))

