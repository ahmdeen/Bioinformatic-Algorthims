"""
Longest Shared Substring Problem

Find the longest substring shared by two strings.

Given: Strings Text1 and Text2.

Return: The longest substring that occurs in both Text1 and Text2.
"""
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

		#print ['','$'][string[-1] != '$']
		#self._list.append(word)
		if type(string) is str:

			string = string + ['','$'][string[-1] != '$'] + str(len(self._list))
			self._list.append(string)
		else:
			for word in string:
				string = word + ['','$'][word[-1] != '$'] + str(len(self._list))
				print string
				#print word
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

"""

#!/usr/bin/env python
'''A Rosalind bioinformatics script containing a generalized suffix tree data structure class.'''


class Node(object):
    """Node class to be used in the GeneralizedSuffixTree class."""
    def __init__(self, parent_num, words=set()):
        """Initialize parameters."""
        self._parent = parent_num
        self._children = []
        self._words = words

    @property
    def parent(self):
        """Parent node getter."""
        return self._parent

    @property
    def children(self):
        """Children nodes getter."""
        return self._children

    @property
    def words(self):
        """Words passing through node getter."""
        return self._words


class Edge(object):
    """Edge class to be used in the GeneralizedSuffixTree class."""
    def __init__(self, word, start_index, stop_index):
        """Initialize parameters."""
        self._word = word
        self._start_index = start_index
        self._stop_index = stop_index


class GeneralizedSuffixTree(object):
    """Constucts a generalized suffix tree for the given words."""
    def __init__(self, words):
        """Initialize parameters and build the tree with the given words."""

        # Initialize parameters.
        self._word_list = []
        self._nodes = [Node(-1)]
        self._edges = {}

        # Add the words to the generalized suffix tree.
        if type(words) is str:
            self._add_word(words)
        else:
            for word in words:
                self._add_word(word)

    @property
    def nodes(self):
        """nodes getter."""
        return self._nodes

    @property
    def edges(self):
        """edges getter."""
        return self._edges

    def _add_word(self, current_word):
        """Adds a word to the generalized suffix tree."""

        # Add the properly indexed out of alphabet character to the current word, and add it to the word list and root node.
        # These need to be distinct (i.e. $0, $1, ..., $N), to distinguish between multiple words in the tree.
        current_word = current_word + ['', '$'][current_word[-1] != '$'] + str(len(self._word_list))
        self._word_list.append(current_word)

        # Add each suffix to the generalized suffix tree.
        for i in xrange(current_word.index('$')+1):
            # Get the insertion point and associated suffix.
            insertion_suffix, insertion_parent = self._insert_node(current_word[i:])

            # Create the new node, and add it as a child to its parent node.
            self._nodes.append(Node(insertion_parent, {len(self._word_list)-1}))
            self._nodes[insertion_parent]._children.append(len(self._nodes)-1)

            # Create the edge associated to with the new node.
            self._edges[insertion_parent, len(self._nodes)-1] = Edge(len(self._word_list)-1, len(current_word)-len(insertion_suffix), len(current_word))

    def _insert_node(self, suffix, current_node=0):
        """Traverses the tree to determine the insertion point of the given suffix."""

        # Mark the word we're adding as traversing through the current node.
        self._nodes[current_node]._words.add(len(self._word_list)-1)

        # Done if we've reached the out of alphabet character.
        if suffix[0] == '$':
            return suffix, current_node

        # Check all childen nodes to determine if we can traverse further down the tree.
        for child_num in self._nodes[current_node]._children:
            e = self._edges[current_node, child_num]
            e_substring = self.edge_substring(e)

            # If the entire edge appears as a prefix of the suffix, move to the child node and traverse further down the tree.
            if suffix[:len(e_substring)] == e_substring:
                return self._insert_node(suffix[len(e_substring):], child_num)

            # If the edge partially overlaps in prefix of the current suffix, split the edge and insert at the split.
            elif suffix[0] == e_substring[0]:
                # Determine how many charaters overlap.
                i = 0
                while suffix[i] == e_substring[i] != '$':
                    i += 1

                # Split the edge at the end of the overlap.
                return suffix[i:], self._split_edge(current_node, child_num, i)

        return suffix, current_node

    def _split_edge(self, parent_num, child_num, split_pos):
        """
        Splits the edge between the given parent and child nodes at the given split position.
        Inserts a new node at the split position and returns the index of the new node.
        """

        # Create the new node.
        new_node = len(self._nodes)
        self._nodes.append(Node(parent_num, words={len(self._word_list)-1} | self._nodes[child_num]._words))
        self._nodes[new_node]._children.append(child_num)

        # Add new_node as a child of parent_num.  Remove child_num from children list.
        self._nodes[parent_num]._children.append(new_node)
        self._nodes[parent_num]._children.remove(child_num)

        # Update child_num's parent to new_node.
        self._nodes[child_num]._parent = new_node

        # Create the new edges.
        old_edge = self._edges[parent_num, child_num]
        self._edges[parent_num, new_node] = Edge(old_edge._word, old_edge._start_index, old_edge._start_index + split_pos)
        self._edges[new_node, child_num] = Edge(old_edge._word, old_edge._start_index + split_pos, old_edge._stop_index)

        # Remove the old edge.
        del self._edges[parent_num, child_num]

        return new_node

    def edge_substring(self, e):
        """Returns the substring associated with a given edge."""
        return self._word_list[e._word][e._start_index:e._stop_index]

    def node_substring(self, node_num):
        """Returns the substring associated with a traversal to the given node."""
        node_word = ''
        while self._nodes[node_num]._parent != -1:
            # Prepend the substring associated with each edge until we hit the root of the generalized suffix tree.
            node_word = self.edge_substring(self._edges[self._nodes[node_num]._parent, node_num]) + node_word
            node_num = self._nodes[node_num]._parent

        return node_word

    def node_depth(self, node_num):
        """
        Returns the length of the substring traversal up to the given node,
        discounting the out of alphabet character, and without constructing the entire word.
        """

        # Trivially have depth zero if at the root.
        if node_num == 0:
            return 0

        # The first edge (working backwards) is the only one that can have an out of alphabet character, so take extra precaution.
        first_edge = self.edge_substring(self._edges[self._nodes[node_num]._parent, node_num])
        depth = len(first_edge) if '$' not in first_edge else len(first_edge[:first_edge.index('$')])

        # Move to the parent node and add the length of the next edge until we hit the root.
        node_num = self._nodes[node_num]._parent
        while self._nodes[node_num]._parent != -1:
            # Prepend the substring associated with each edge until we hit the root of the generalized suffix tree.
            depth += len(self.edge_substring(self._edges[self._nodes[node_num]._parent, node_num]))
            node_num = self._nodes[node_num]._parent

        return depth

def longestSharedSub(Texts):
   

    sTree = GeneralizedSuffixTree(Texts)

    candidates = filter(lambda i: len(sTree.nodes[i].words) == len(Texts), xrange(len(sTree.nodes)))

    deepest = max(candidates, key=lambda i: sTree.node_depth(i))

    return sTree.node_substring(deepest)

#with open('Data/rosalind_7e.txt') as infile:
#	text = [line.strip() for line in infile]
	#print text
text = ['TCGGTAGATTGCGCCCACTC',
'AGGGGCTCGCAGTGTAAGAA']

answer = longestSharedSub(text)

print answer

with open('Ros7E_Answer.txt','w') as outfile:
	outfile.write(answer)

