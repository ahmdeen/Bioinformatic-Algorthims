"""
Suffix Array Construction Problem

Construct the suffix array of a string.

Given: A string Text.

Return: SuffixArray(Text).
"""

def suffixArrayConstruct(text):

	text += ['', '$'][text[-1] != '$']

   
	suffComp = lambda i,j: [1, -1][text[i] < text[j]] if text[i] != text[j] else suffComp(i+1,j+1)

	suffixArray = sorted(xrange(len(text)), cmp=suffComp)

	return suffixArray

with open('Data/rosalind_7g.txt') as infile:
	text = infile.read().strip()

answer = map(str, suffixArrayConstruct(text))

print ', '.join(answer)

with open('Ros7G_Answer.txt','w') as outfile:
	outfile.write(', '.join(answer))
