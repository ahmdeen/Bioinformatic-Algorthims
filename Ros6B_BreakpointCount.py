"""
Number of Breakpoints Problem

Find the number of breakpoints in a permutation.

Given: A signed permutation P.

Return: The number of breakpoints in P.
"""

'''Functions'''

def BreakpointCount(P):

	fcn = lambda x, y: x - y != 1

	return sum(map(fcn, P + [len(P) + 1], [0]+P))


'''Input/ Output'''
with open('Data/rosalind_6b.txt') as infile:
	p = map(int, infile.read().strip().lstrip('(').rstrip(')').split())

answer = BreakpointCount(p)

print str(answer)

with open('Ros6b_Answer.txt','w') as outfile:
	outfile.write(str(answer))

