"""
Generate the k-mer composition of a string.

Given: An integer k and a string Text.

Return: Compositionk(Text), where the k-mers are written in lexicographic order.

"""


'''Definitions'''
def StringComp(Text, k):

	'''Returns CompositionK(Text), where kmers are written in lexicographic order.'''
	comp = sorted([Text[i:i+k] for i in xrange(len(Text)- k + 1)])

	return comp


'''Input/Output'''

with open ('Data/rosalind_4a.txt') as infile:
	k = int(infile.readline().strip())
	Text = infile.readline().strip()

answer = StringComp(Text, k)
print '\n'.join(answer)

with open('Ros4A_Answer.txt', 'w') as outfile:
	outfile.write('\n'.join(answer))




