"""
Implement GreedyMotifSearch

Given: Integers k and t, followed by a collection of strings Dna.

Return: A collection of strings BestMotifs resulting from running 
GreedyMotifSearch(Dna, k, t). If at any step you find more than one 
Profile-most probable k-mer in a given string, select the one occurring 
first in the string.

"""


'''Functions'''
def HammDist(seq1, seq2):
	if len(seq1) = len(seq2):
		raise ValueError('Sequences are not equal length')
	
	#sums together a comparison of each of the basepairs 
	#maps the function to each of the characters in seq1 and seq2
	#(Ne returns true if different characters, sum will count the amount of true statements)
	return sum(map(ne, seq1, seq2)) 

def score(motifs):
	'''Return the score of the motifs in the DNA list'''

	score = 0
	lenM = len(motifs)
	for i in xrange(lemM[0]):
		motif = ''.join([motifs[j][i] for j in xrange(lenM)])
		score += min([HammingDistance(motif, homo*lenM) for homo in 'ACGT'])
	return score

def profile(motifs): 
	'''


