"""
Trie Construction Problem

Construct a trie on a collection of patterns.

Given: A collection of strings Patterns.

Return: The adjacency list corresponding to Trie(Patterns), in the following format. 
If Trie(Patterns) has n nodes, first label the root with 1 and then label the remaining nodes with the integers 
2 through n in any order you like. Each edge of the adjacency list of Trie(Patterns) will be encoded by a triple: 
the first two members of the triple must be the integers labeling the initial and terminal nodes of the edge, respectively; 
the third member of the triple must be the symbol labeling the edge.
"""


'''Classes'''

class Ros_Trie(object):
	'''Construct a Trie for the given input strings'''

	def __init__(self, strings):
		'''Initialize function to intialize the nodes and edges, adding the given strings'''

		self.initNode = lambda p, d: {'parent': p, 'children':[], 'depth': d, 'last':False}
			#parent = parent index
			#children = list of all children of p indices
			#depth = length of substring up till nodes
			#last = boolean to check if the current node corresponds to last character of the input strings

		self.nodes = {1:self.initNode(0,0)}
		self.edges = {}
		#print self.nodes
		if type(strings) is str:
			self._addString(strings)
		else: 
			for string in strings:
				self._addString(string)


	def _addString(self, string):
		'''Adds the current string to trie'''

		#Grab Insertion Node Location and substring of word to insert
		insertNode, insertSubstring = self._insertLoc(string)
		

		#Insert at the insertion node
		for i in xrange(len(insertSubstring)):
			#Get the new node number
			newNode = len(self.nodes) + 1 # basically the next node


			self.nodes[newNode] = self.initNode(insertNode, self.nodes[insertNode]['depth']+1)
			self.nodes[insertNode]['children'].append(newNode)

			#print insertNode, newNode
			
			#Add the new node to the trie
			self.edges[insertNode, newNode] = insertSubstring[i]
			print insertNode -1, newNode-1, insertSubstring[i]
			#Increment to the new node and continue insertion
			insertNode = newNode

		#print self.nodes
		self.nodes[insertNode]['last'] = True #since it is now the last node, and the end of the string END OF THE LINE!!!


	def _insertLoc(self, string, thisNode=1):
		'''Traverses the Trie and finds the insertion point for the given string'''

		#edge case where if input string is already a substring of a previous string
		if string  == '':
			#print thisNode, string
			return thisNode, string

		#iterate and search through all child nodes
		for child in self.nodes[thisNode]['children']:
			if self.edges[thisNode, child] == string[0]:
				#shift to child node for match
				#print self._insertLoc(string[1:], child)
				return self._insertLoc(string[1:], child)

		#print thisNode, string
		return thisNode, string


	def up2Node(self, node1):
		'''Returns the string traversing til the input node'''

		nodeString = ''
		while self.nodes[node1]['parent'] != 0:
			nodeString += self.edges[self.node[node1]['parent'], node1]
			node1 = self.nodes[node1]['parent']


		return nodeString[::-1]

	def checkPrefix(self, string, thisNode = 1):
		'''Traverses the trie to see if a prefix of the given string matches a pattern in the trie'''

		if self.nodes[thisNode]['last'] == True:
			#We hit an end node, found a matching pattern as a prefix
			return True

		elif string == '':
			return False

		#Search through all child nodes

		for child in self.nodes[thisNode]['children']:
			if self.edges[thisNode, child] == string[0]:
				#Move to child if theres a match

				return self.checkPrefix(string[1:], child)

		#Only reach if there is no chartacter match, therefor no prefix
		return False



'''Functions'''

def trieEdges(patterns):
	'''Returns the edges of a trie as constructed from the input string; output is adjacency list'''

	#Initialize the Trie

	t = Ros_Trie(patterns)

	minuser = lambda x: x-1
	adjacencyList = lambda node: '->'.join(map(str,map(minuser,node[0]))) + ':' + node[1]


	return map(adjacencyList, t.edges.items())


with open('Data/rosalind_7a.txt') as infile:
	patterns = [line.strip() for line in infile.readlines()]
#patterns = ['ATAGA','ATC','GAT']

answer = trieEdges(patterns)

print '\n'.join(answer)
with open('Ros7a_Answer.txt','w') as outfile:
	outfile.write('\n'.join(answer))