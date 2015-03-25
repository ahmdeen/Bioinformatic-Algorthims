"""
2-Break Distance Problem

Find the 2-break distance between two genomes.

Given: Two genomes with circular chromosomes on the same set of synteny blocks.

Return: The 2-break distance between these genomes.
"""

from collections import defaultdict

'''Functions'''

def twoBreakDist(P, Q):

	bpGraph = defaultdict(list)
	for pCycle in P+Q: 
		n = len(pCycle)
		for i in xrange(n):

			bpGraph[pCycle[i]].append(-1*pCycle[(i+1)%n])
			bpGraph[-1*pCycle[(i+1)%n]].append(pCycle[i])

	#connected component counter and remaining components
	compCounter = 0 
	compRemain = set(bpGraph.keys())

	while compRemain:
		compCounter += 1
		queue = {compRemain.pop()}

		while queue:
			current = queue.pop()
			new = {node for node in bpGraph[current] if node in compRemain}

			queue |= new
			compRemain -= new

	return sum(map(len, P)) - compCounter

'''Input/Output'''

with open('Data/rosalind_6c.txt') as infile:
	P, Q = [line.strip().lstrip('(').rstrip(')').split(')(') for line in infile]
	#P = infile.readline().strip().lstrip('(').rstrip(')').split()
	#Q = infile.readline().strip().lstrip('(').rstrip(')').split()
	#print P, Q
	P = [map(int, cycle.split()) for cycle in P]
	Q = [map(int, cycle.split()) for cycle in Q]

	#print P, Q
"""
string1 = "(+1 +2 +3 +4 +5 +6)"
string2 = "(+1 -3 -6 -5)(+2 -4)"

P = string1.strip().lstrip('(').rstrip(')').split(')(')
Q = string2.strip().lstrip('(').rstrip(')').split(')(')

P = [map(int, cycle.split()) for cycle in P]
Q = [map(int, cycle.split()) for cycle in Q]
"""
print P, Q
answer = twoBreakDist(P, Q)

print str(answer)

with open('Ros6C_Answer.txt','w') as outfile:
	outfile.write(str(answer))