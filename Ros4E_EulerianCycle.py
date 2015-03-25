"""
Eulerian Cycle Problem

Find an Eulerian cycle in a graph.

Given: An Eulerian directed graph, in the form of an adjacency list.

R
"""

'''Functions'''
"""
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
					cycle.append(edges[thisNode][0])
					
					if len(edges[thisNode]) == 1:
						del edges[thisNode]
					else:
						edges[thisNode] = edges[thisNode][1:]

					if cycle[-1] in edges:
						thisnode = cycle[-1]
					else:
						break

				epath = ePath[:i] + cycle + ePath[i+1:]
				break
	return ePath

"""
def eulerian_cycle(edge_dict):
    '''Generates an Eulerian cycle from the given edges.'''
    current_node = edge_dict.keys()[0]
    path = [current_node]

    # Get the initial cycle.
    while True:
        path.append(edge_dict[current_node][0])

        if len(edge_dict[current_node]) == 1:
            del edge_dict[current_node]
        else:
            edge_dict[current_node] = edge_dict[current_node][1:]

        if path[-1] in edge_dict:
            current_node = path[-1]
        else:
            break

    # Continually expand the initial cycle until we're out of edge_dict.
    while len(edge_dict) > 0:
        for i in xrange(len(path)):
            if path[i] in edge_dict:
                current_node = path[i]
                cycle = [current_node]
                while True:
                    cycle.append(edge_dict[current_node][0])

                    if len(edge_dict[current_node]) == 1:
                        del edge_dict[current_node]
                    else:
                        edge_dict[current_node] = edge_dict[current_node][1:]

                    if cycle[-1] in edge_dict:
                        current_node = cycle[-1]
                    else:
                        break

                path = path[:i] + cycle + path[i+1:]
                break
    return path
"""
"""
'''Input/Output'''

with open('Data/rosalind_4e.txt') as infile:
	edges = {}

	for edge in [line.strip().split(' -> ') for line in infile.readlines()]:
		if ',' in edge[1]:
			edges[int(edge[0])] = map(int,edge[1].split(','))
		else:
			edges[int(edge[0])] = [int(edge[1])]

#answer = EulerianCycle(edges)
answer = eulerian_cycle(edges)
#print '->'.join(map(str,answer))

with open('Ros4E_Answer.txt', 'w') as outfile:
	outfile.write('->'.join(map(str,answer)))


