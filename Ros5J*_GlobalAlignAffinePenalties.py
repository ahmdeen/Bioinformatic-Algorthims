"""
Alignment with Affine Gap Penalties Problem

Construct a highest-scoring global alignment of two strings (with affine gap penalties).

Given: Two amino acid strings v and w (each of length at most 100).

Return: The maximum alignment score between v and w, followed by an alignment of v and w 
achieving this maximum score. Use the BLOSUM62 scoring matrix, a gap opening penalty of 11, 
and a gap extension penalty of 1.

"""

import os

'''Classes'''
class blosum62(object):
	'''Class to score proteins using the BLOSUM62 matrix'''

	def __init__(self):
		'''Initalize BLOSUM62 Matrix'''
		with open(os.path.join(os.path.dirname(__file__), 'DATA/BLOSUM62.txt')) as inFile:
			lines = [line.strip().split() for line in inFile.readlines()]
			self.S = {(item[0], item[1]): int(item[2]) for item in lines} 

	def __getitem__(self, pair):
		'''Returns the score of a given pair'''
		return self.S[pair[0],pair[1]]


'''Functions'''

def global_alignment_affine_gap_penalty(v, w, scoring_matrix, sigma, epsilon):
    '''Returns the global alignment score of v and w with constant gap peantaly sigma subject to the scoring_matrix.'''
    # Initialize the matrices.
    S = [[[0 for j in xrange(len(w)+1)] for i in xrange(len(v)+1)] for k in xrange(3)]
    backtrack = [[[0 for j in xrange(len(w)+1)] for i in xrange(len(v)+1)] for k in xrange(3)]

    # Initialize the edges with the given penalties.
    for i in xrange(1, len(v)+1):
		S[0][i][0] = -sigma - (i-1)*epsilon
        S[1][i][0] = -sigma - (i-1)*epsilon
        S[2][i][0] = -10*sigma
	for j in xrange(1, len(w)+1):
		S[2][0][j] = -sigma - (j-1)*epsilon
       	S[1][0][j] = -sigma - (j-1)*epsilon
       	S[0][0][j] = -10*sigma

   # Fill in the scores for the lower, middle, upper, and backtrack matrices.
	for i in xrange(1, len(v)+1):
 	   	for j in xrange(1, len(w)+1):
			lower_scores = [S[0][i-1][j] - epsilon, S[1][i-1][j] - sigma]
           	S[0][i][j] = max(lower_scores)
           	backtrack[0][i][j] = lower_scores.index(S[0][i][j])

           	upper_scores = [S[2][i][j-1] - epsilon, S[1][i][j-1] - sigma]
           	S[2][i][j] = max(upper_scores)
           	backtrack[2][i][j] = upper_scores.index(S[2][i][j])

           	middle_scores = [S[0][i][j], S[1][i-1][j-1] +scoring_matrix[v[i-1], w[j-1]], S[2][i][j]]
           	S[1][i][j] = max(middle_scores)
           	backtrack[1][i][j] = middle_scores.index(S[1][i][j])

  	# Initialize the values of i, j and the aligned sequences.
   	i,j = len(v), len(w)
   	v_aligned, w_aligned = v, w

   	# Get the maximum score, and the corresponding backtrack starting position.
   	matrix_scores = [S[0][i][j], S[1][i][j], S[2][i][j]]
   	max_score = max(matrix_scores)
   	backtrack_matrix = matrix_scores.index(max_score)

   	# Quick lambda function to insert indels.
   	insert_indel = lambda word, i: word[:i] +'-' +word[i:]

   	# Backtrack to the edge of the matrix starting bottom right.
   	while i*j != 0:
    	if backtrack_matrix == 0:  # Lower backtrack matrix conditions.
           	if backtrack[0][i][j] == 1:
               backtrack_matrix = 1
           	i -= 1
           	w_aligned = insert_indel(w_aligned, j)

       	elif backtrack_matrix == 1:  # Middle backtrack matrix conditions.
           	if backtrack[1][i][j] == 0:
               backtrack_matrix = 0
           	elif backtrack[1][i][j] == 2:
               backtrack_matrix = 2
           	else:
               	i -= 1
               	j -= 1

       	else:  # Upper backtrack matrix conditions.
           	if backtrack[2][i][j] == 1:
               backtrack_matrix = 1
           j -= 1
           v_aligned = insert_indel(v_aligned, i)

   # Prepend the necessary preceeding indels to get to (0,0).
   for _ in xrange(i):
       w_aligned = insert_indel(w_aligned, 0)
   for _ in xrange(j):
       v_aligned = insert_indel(v_aligned, 0)

   return str(max_score), v_aligned, w_aligned

'''Input/Output'''

#with open('Data/rosalind_5j.txt') as infile:
#	seq1, seq2 = [line.strip() for line in infile.readlines()]


seq1 = 'PRTEINS'
seq2 = 'PRTWPSEIN'
answer = globalAlignAffine(seq1, seq2, blosum62(), 11, 1)

print '\n'.join(answer)

with open('Ros5j_Answer', 'w') as outfile:
	outfile.write('\n'.join(answer))
		
		
