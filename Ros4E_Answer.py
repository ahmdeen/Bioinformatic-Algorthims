"""
Eulerian Cycle Problem

Find an Eulerian cycle in a graph.

Given: An Eulerian directed graph, in the form of an adjacency list.

Return: An Eulerian cycle in this graph.

"""

'''Functions'''

def EulerianCycle(edges):
	'''Creates a EulerianCycle from the given edges'''
	thisNode = edges.keys()[0]
	ePath = [thisNode]

	while True:
		ePath.append(edges[thisNode][0])

		if len(edges[thisNode]) == 1:
			del edges[thisNode]
		else:
			edges[thisNode] = edges[thisNode][1:]

		if ePath[-1] in edges:
			thisNode = ePath[-1]
		else:
			break

	while len(edges) > 0:
		for i in xrange(len(ePath)):
			if ePath[i] in edges:
				thisNode = ePath[i]
				cycle = [thisNode]
				while True:
					cycle.append(edges[thisnode][0])
					
					if len(edges[thisNode] == 1):
						del edges[thisNode]
					else:
						edges[thisNode] = edges[thisNode][1:]

					if cycle[-1] in edges:
						thisnode = cycle[-1]
					else:
						break

				path = ePath[:i] + cycle + ePath[i+1:]
				break
	return ePath

'''Input/Output'''

with open('Data/rosalind_4e.txt') as infile:
	edges = {}

	for edge in [line.strip().split(' -> ') for line in infile.readlines()]:
		if ',' in edge[1]:
			edges[int(edge[0])] = map(int,edge[1].split(','))
		else:
			edges[int(edge[0])] = [int(edge[1])]

answer = EulerianCycle(edges)

print '->'.join(map(str,answer))

with open('Ros4E_Answer.txt', 'w') as outfile:
	outfile.write('->'.join(map(str,answer)))


