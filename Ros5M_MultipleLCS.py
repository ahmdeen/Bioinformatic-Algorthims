"""

"""

def multipleAlignment(seq1, seq2, seq3):
    '''Returns the alignment of three sequences v, w, and u.'''
    # Initialize the matrices.
    len1, len2, len3 = len(seq1), len(seq2), len(seq3)
    S = [[[0 for k in xrange(len3 + 1)] for j in xrange(len2+1)] for i in xrange(len1+1)]
    backtrack = [[[0 for k in xrange(len3+1)] for j in xrange(len2+1)] for i in xrange(len1+1)]

    # Fill in the Score and Backtrack matrices.
    for i in xrange(1, len1+1):
        for j in xrange(1, len2+1):
            for k in xrange(1, len3+1):
                scoreList = [S[i-1][j-1][k-1] + int(seq1[i-1] == seq2[j-1] == seq3[k-1]), S[i-1][j][k], S[i][j-1][k], S[i][j][k-1], S[i-1][j][k-1], S[i][j-1][k-1]]
                backtrack[i][j][k], S[i][j][k] = max(enumerate(scoreList), key=lambda p: p[1])

    
    insertIndelFcn = lambda seq, i: seq[:i] + '-' + seq[i:]

    # Initialize the alignment string
    align1, align2, align3 = seq1, seq2, seq3

    
    a, b, c= len1, len2, len3
    maxScore = S[a][b][c]

    # Backtrack to the edge of the matrix 
    while a*b*c != 0:
        if backtrack[a][b][c] == 1:
            a -= 1
            align2 = insertIndelFcn(align2, b)
            align3 = insertIndelFcn(align3, c)
        elif backtrack[a][b][c] == 2:
            b -= 1
            align1 = insertIndelFcn(align1, a)
            align3 = insertIndelFcn(align3, c)
        elif backtrack[a][b][c] == 3:
            c -= 1
            align1 = insertIndelFcn(align1, a)
            align2 = insertIndelFcn(align2, b)
        elif backtrack[a][b][c] == 4:
            a -= 1
            b -= 1
            align3 = insertIndelFcn(align3, c)
        elif backtrack[a][b][c] == 5:
            a -= 1
            c -= 1
            align2 = insertIndelFcn(align2, b)
        elif backtrack[a][b][c] == 6:
            b -= 1
            c -= 1
            align1 = insertIndelFcn(align1, a)
        else:
            a -= 1
            b -= 1
            c -= 1

    # Prepend the necessary preceeding indels to get match lengths.
    while len(align1) != max(len(align1),len(align2),len(align3)):
        align1 = insertIndelFcn(align1, 0)
    while len(align2) != max(len(align1),len(align2),len(align3)):
        align2 = insertIndelFcn(align2, 0)
    while len(align3) != max(len(align1),len(align2),len(align3)):
        align3 = insertIndelFcn(align3, 0)

    return str(maxScore), align1, align2, align3

'''Input/Output'''

#with open('Data/rosalind_5m.txt') as infile:
#	seq1, seq2, seq3 = [line.strip() for line in infile]

answer = multipleAlignment(seq1, seq2, seq3)

print '\n'.join(answer)

with open('Ros5m_Answer.txt', 'w') as outfile:
	outfile.write('\n'.join(answer))