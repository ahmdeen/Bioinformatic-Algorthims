"""
Implement TrieMatching

Given: A string Text and a collection of strings Patterns.

Return: All starting positions in Text where a string from Patterns appears as a substring.
"""

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
			
			#Add the new node to the trie
			self.edges[insertNode, newNode] = insertSubstring[i]
			#Increment to the new node and continue insertion
			insertNode = newNode

		self.nodes[insertNode]['last'] = True #since it is now the last node, and the end of the string END OF THE LINE!!!


	def _insertLoc(self, string, thisNode=1):
		'''Traverses the Trie and finds the insertion point for the given string'''

		#edge case where if input string is already a substring of a previous string
		if string  == '':
			return thisNode, string

		#iterate and search through all child nodes
		for child in self.nodes[thisNode]['children']:
			if self.edges[thisNode, child] == string[0]:
				#shift to child node for match
				return self._insertLoc(string[1:], child)

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


def trieMatching(Text, Patterns):

	'''Returns the starting index of all the locations in Text where a pattern in patterns is a substring'''

	t = Ros_Trie(Patterns)

	indices = [i for i in xrange(len(Text)-min(map(len,Patterns))+1) if t.checkPrefix(Text[i:]) is True]

	return indices

with open('Data/rosalind_7b.txt') as infile:
	text = infile.readline().strip()
	patterns = [line.strip() for line in infile.readlines()]


answer = trieMatching(text, patterns)

print ' '.join(map(str, answer))

with open('Ros7b_Answer.txt','w') as outfile:
	outfile.write(' '.join(map(str,answer)))

