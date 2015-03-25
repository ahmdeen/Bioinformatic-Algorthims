"""
We say that a k-mer is shared by two genomes if either the k-mer or its reverse complement appears in each genome. 
In Figure 1 are four pairs of 3-mers that are shared by "AAACTCATC" and "TTTCAAATC".

Figure1: http://rosalind.info/media/problems/6d/shared_k-mers.thumb.png

A shared k-mer can be represented by an ordered pair (x, y), 
where x is the starting position of the k-mer in the first genome and y is the starting position of the k-mer 
in the second genome. For the genomes "AAACTCATC" and "TTTCAAATC", these shared k-mers are (0,4), (0,0), (4,2), and (6,6).

Shared k-mers Problem

Given two strings, find all their shared k-mers.

Given: An integer k and two strings.

Return: All k-mers shared by these strings, in the form of ordered pairs (x, y).

"""

from collections import defaultdict
from string import maketrans


'''Functions'''

def dnaPolymerase(DNA):
	DNA.upper()
	parentBase = 'ATCG'
	complementBase = 'TAGC'
	transTable = maketrans(parentBase, complementBase)

	return DNA.translate(transTable)[::-1].lstrip()

def sharedKmers(k, seq1, seq2):

	dict1 = defaultdict(list)
	for i in xrange(len(seq1)-k+1):
		dict1[seq1[i:i+k]].append(i)

	return {(i,j) for j in xrange(len(seq2)-k+1) for i in dict1[seq2[j:j+k]] + dict1[dnaPolymerase(seq2[j:j+k])]}

'''Input/Output'''

with open('Data/rosalind_6d.txt') as infile:
	k = int(infile.readline().strip())
	seq1, seq2 = [line.strip() for line in infile.readlines()]


answer = map(str, sorted(sharedKmers(k, seq1, seq2)))

with open('Ros6d_Answer.txt', 'w') as outfile:
	outfile.write('\n'.join(answer))