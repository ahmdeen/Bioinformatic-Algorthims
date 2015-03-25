"""
Inverse Burrows-Wheeler Transform Problem

Reconstruct a string from its Burrows-Wheeler transform.

Given: A string Transform (with a single "$" sign).

Return: The string Text such that BWT(Text) = Transform.
"""


def inverseBWT(bwt):

	enumBWT = enum(bwt)
	enumSort = enum(sorted(bwt))

	inverseDict = {enumBWT[i]:enumSort[i] for i in xrange(len(bwt))}
	inverse = ''

	current = enumBWT[0]
	for i in xrange(len(bwt)):
		current = inverseDict[current]
		inverse += current[0]

	return inverse[1:]+inverse[0]

def enum(text):

	chCount = {}
	enumerated = []

	for character in text:
		if character not in chCount:
			chCount[character] = 0
		else:
			chCount[character] += 1

		enumerated.append(character + str(chCount[character]))

	return enumerated

with open('Data/rosalind_7J.txt') as infile:
	bwt = infile.read().strip()

answer = inverseBWT(bwt)

print answer

with open('Ros7J_Answer.txt','w') as outfile:

	outfile.write(answer)

