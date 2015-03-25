"""
Shortest Non-Shared Substring Problem

Find the shortest substring of one string that does not appear in another string.

Given: Strings Text1 and Text2.

Return: The shortest substring of Text1 that does not appear in Text2.

"""

class Node(object):

	'''Node Class for Suffix Tree'''

	def __init__(self, Parent, Text=set()):
		self._parent = Parent
		self._children = []
		self._text = Text

	@property
	def parent(self):
		'''Parent node getter fcn'''

		return self._parent

	@property
	def children(self):
		'''Children node getter'''

		return self._children

	@property
	def text(self):
		'''text passing through node getter'''

		return self._text

class Edge(object):
	'''Edge class for Suffix Tree'''

	def __init__(self, Text, startInd, stopInd):
		self._text = Text
		self._start = startInd
		self._stop = stopInd

class Ros_SuffixTree(object):
	'''Constructs a generalized suffix tree for the given text'''

	def __init__(self, text):
		self._list = []
		self._nodes = [Node(-1)]
		self._edges = {}

		if type(text) is str:
			self._addString(text)
		else:
			for string in text:
				self._addString(text)

	@property
	def nodes(self):
		'''node getter'''
		return self._nodes

	@property
	def edges(self):
		'''edges getter'''
		return self._edges

	def _addString(self, string):
		string = string + ['','$'][string[-1] != '$'] + str(len(self._list))
		self._list.append(string)

		for i in xrange(string.index('$')+1):
			insertSuffix, insertParent = self._insertNode(string[i:])

			self._nodes.append(Node(insertParent, {len(self._list)-1}))
			self._nodes[insertParent]._children.append(len(self._nodes)-1)

			self._edges[insertParent, len(self._nodes)-1] = Edge(len(self._list)-1, len(string)-len(insertSuffix), len(string))

	def _insertNode(self, suffix, thisNode=0):

		self._nodes[thisNode]._text.add(len(self._list)-1)

		if suffix[0] == '$':
			return suffix, thisNode

		for child in self._nodes[thisNode]._children:
			edge = self._edges[thisNode, child]
			edgeSub = self.edgeSubstring(edge)

			if suffix[:len(edgeSub)] == edgeSub:
				return self._insertNode(suffix[len(edgeSub):], child)

			elif suffix[0] == edgeSub[0]:
				i = 0
				while suffix[i] == edgeSub[i] != '$':
					i += 1

				return suffix[i:], self._splitEdge(thisNode, child, i)

		return suffix, thisNode

	def _splitEdge(self, parent, child, position):

		newNode = len(self._nodes)
		self._nodes.append(Node(parent, Text={len(self._list)-1} | self._nodes[child]._text))
		self._nodes[newNode]._children.append(child)

		self._nodes[parent]._children.append(newNode)
		self._nodes[parent]._children.remove(child)

		self._nodes[child]._parent = newNode

		edgeOld = self._edges[parent, child]
		self._edges[parent, newNode] = Edge(edgeOld._text, edgeOld._start, edgeOld._start + position)
		self._edges[newNode, child] = Edge(edgeOld._text, edgeOld._start + position, edgeOld._stop)

		del self.edges[parent, child]

		return newNode

	def edgeSubstring(self, edge):
		return self._list[edge._text][edge._start:edge._stop]

	def nodeSubstring(self, node):

		nodeText = ''
		while self._nodes[node]._parent != -1:

			nodeText = self.edgeSubstring(self._edges[self._nodes[node]._parent, node]) + nodeText
			node = self._nodes[node]._parent

		return nodeText

	def nodeDepth(self, node):

		if node == 0:
			return 0

		firstEdge = self.edgeSubstring(self._edges[self._nodes[node]._parent, node])
		depth = len(firstEdge) if '$' not in firstEdge else len(firstEdge[:firstEdge.index('$')])

		node = self._nodes[node]._parent

		while self._nodes[node]._parent != -1:

			depth += len(self.edgeSubstring(self._edges[self._nodes[node]._parent, node]))
			node = self._nodes[node]._parent

		return depth

def shortestNonShared(texts):
    sTree = Ros_SuffixTree(texts)

    candidates = filter(lambda i: sTree.nodes[i].text == {0}, xrange(len(sTree.nodes)))

    candidates = filter(lambda i: sTree.edgeSubstring(sTree.edges[sTree.nodes[i].parent,i]) != '$0', candidates)

    shortest = min(candidates, key=lambda i: sTree.nodeDepth(sTree.nodes[i].parent)+1)

    return sTree.nodeSubstring(sTree.nodes[shortest].parent) + sTree.edgeSubstring(sTree.edges[sTree.nodes[shortest].parent,shortest])[0]

with open('Data/rosalind_7f.txt') as infile:
	text = [line.strip() for line in infile]

answer = shortestNonShared(text)

print answer

with open('Ros7F_Answer.txt','w') as outfile:
	outfile.write(answer)

