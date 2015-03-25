"""
Longest Path in a DAG Problem

Find a longest path between two nodes in an edge-weighted DAG.

Given: An integer representing the source node of a graph, followed by an integer 
representing the sink node of the graph, followed by an edge-weighted graph. 
The graph is represented by a modified adjacency list in which the notation "0->1:7" 
indicates that an edge connects node 0 to node 1 with weight 7.

Return: The length of a longest path in the graph, followed by a longest path. 
(If multiple longest paths exist, you may return any one.)

"""

def topOrder(rawGraph):
	'''Return the input graph topologically ordered'''

	rawGraph = set(rawGraph)
	orderedList = []

	neighbors = list({edge[0] for edge in rawGraph} - {edge [1] for edge in rawGraph})

	while len(neighbors) != 0:
		orderedList.append(neighbors[0])

		nodeStorage = []
		for edge in filter(lambda edgy:edgy[0] == neighbors[0], rawGraph):
			rawGraph.remove(edge)
			nodeStorage.append(edge[1])

		for node in nodeStorage:
			if node not in {edge[1] for edge in rawGraph}:
				neighbors.append(node)

		
		neighbors = neighbors[1:]

	return orderedList

def longestPath(graph, edgeDict, source, sink):
	'''Return the length of the longest path in the graph, followed by a longest path'''
	#print source, sink
	#print graph.keys()
	tlogOrder = topOrder(graph.keys())
	#print tlogOrder
	#tlogSource, tlogSink = tlogOrder.index(source), tlogOrder.index(sink)
	tlogOrder = tlogOrder[tlogOrder.index(source)+1:tlogOrder.index(sink)+1]
	#print tlogOrder

	S = {node:-100 for node in {edge[0] for edge in graph.keys()} | {edge[1] for edge in graph.keys()}}

	S[source] = 0
	bktrack = {node:None for node in tlogOrder}

	#print tlogOrder
	for node in tlogOrder:
		try:
			S[node], bktrack[node] = max(map(lambda edgy: [S[edgy[0]] + graph[edgy], edgy[0]], filter(lambda edgy: edgy[1] == node, graph.keys())), key=lambda l: l[0])
			
		except ValueError:
			pass

	longPath = [sink]
	while longPath[0] != source:
		longPath = [bktrack[longPath[0]]] + longPath

	return S[sink],longPath

with open('Data/rosalind_5d.txt') as inFile:
	source = int(inFile.readline().strip())
	sink = int(inFile.readline().strip())


	edges, weight = {},{}
	for items in [line.strip().split('->') for line in inFile.readlines()]:
		if int(items[0]) not in edges:
			edges[int(items[0])] = [int(items[1].split(':')[0])]
		else:
			edges[int(items[0])].append(int(items[1].split(':')[0]))

		weight[int(items[0]), int(items[1].split(':')[0])] = int(items[1].split(':')[1])

length, lPath = longestPath(weight, edges, source, sink)

length= str(length)
lPath = '->'.join(map(str,lPath))

print'\n'.join([length, lPath])
with open ('Ros5D_Answer.txt', 'w') as outFile:
	outFile.write('\n'.join([length,lPath]))







