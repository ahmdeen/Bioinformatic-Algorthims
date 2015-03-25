"""
Eulerian Path Problem

Find an Eulerian path in a graph.

Given: A directed graph that contains an Eulerian path, where the graph is given in the form of an adjacency list.

Return: An Eulerian path in this graph.

"""

from Ros4E_EulerianCycle import eulerian_cycle

'''Functions'''

def EulerianPath(edges):
	'''Returns a Eulerian Path from the given edges'''

	#Find Unbalanced Edges
	outDegs = reduce (lambda x,y:x+y, edges.values())
	for node in set(outDegs+edges.keys()):
		outDeg = outDegs.count(node)

		if node in edges:
			inDeg = len(edges[node])
		else:
			inDeg = 0

		if inDeg < outDeg:
			unFrom = node
		elif outDeg < inDeg:
			unTo = node

	#Connect unbalanced edges with another edge

	if unFrom in edges:
		edges[unFrom].append(unTo)
	else:
		edges[unFrom] = [unTo]

	#Call Eulerian Cycle using edges, including the unbalanced edge
	cycle = eulerian_cycle(edges)

	#Find the unbalanced edge in the cycle
	divPoint = filter(lambda i:cycle[i:i+2] == [unFrom, unTo], xrange(len(cycle)-1))[0]

	#Remove the unbalanced edge, and adjust accordinly with overlap for the head and tail
	return cycle[divPoint+1:]+cycle[1:divPoint+1]

'''Input/Output'''

with open('Data/rosalind_4f.txt') as infile:
	edges = {}
	for edge in [line.strip().split(' -> ') for line in infile.readlines()]:
		#print edge
		if ',' in edge[1]:
			edges[int(edge[0])] = map(int,edge[1].split(','))
		else:
			edges[int(edge[0])] = [int(edge[1])]

answer = EulerianPath(edges)
print '->'.join(map(str,answer))

with open('Ros4F_Answer.txt','w') as outfile:
	outfile.write('->'.join(map(str,answer)))