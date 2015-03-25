"""
Burrows-Wheeler Transform Construction Problem

Construct the Burrows-Wheeler transform of a string.

Given: A string Text.

Return: BWT(Text).
"""

def BWT(text):

	text += ['', '$'][text[-1] != '$']

	lenT = len(text)

	cyIndex = lambda i, n: text[(n-i)%lenT]

	cyComp = lambda i, j, n=0: [1,-1][cyIndex(i,n) < cyIndex(j,n)] if cyIndex(i,n) != cyIndex(j,n) else cyComp(i,j, n+1)

	cySort = sorted(xrange(len(text)), cmp = cyComp) 

	return ''.join([cyIndex(i,-1) for i in cySort])

with open('Data/rosalind_7I.txt') as infile:
	Text = infile.read().strip()

answer = BWT(Text)

print answer

with open('Ros7I_Answer.txt','w') as outfile:
	outfile.write(answer)