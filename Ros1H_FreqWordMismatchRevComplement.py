"""
Frequent Words with Mismatches and Reverse Complements Problem

Find the most frequent k-mers (with mismatches and reverse complements) in a DNA string.

Given: A DNA string Text as well as integers k and d.

Return: All k-mers Pattern maximizing the sum Countd(Text, Pattern) + Countd(Text, Pattern) over all possible k-mers.

"""

from collections import defaultdict
from Ros1G_FreqWordMismatches import kmerMismatcher


def RevComp(Pattern):
	Complement = []

	Bases = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

	for i in Pattern:
		Complement.append(Bases[i])

	Complement.reverse()

	#print "".join(Complement)
	return Complement 

def fWordsMismatch_and_RevComp(Text, k, d):

	kmerFreq = defaultdict(int)
	for i in xrange(len(Text) - k +1):
		kmerFreq[Text[i:i+k]] += 1
		revComplement = ''.join(RevComp(Text[i:i+k]))


		kmerFreq[revComplement] += 1

	mismatchCounter = defaultdict(int)
	for kmer, frequency in kmerFreq.iteritems():
		for mismatch in kmerMismatcher(kmer, d):
			mismatchCounter[mismatch] += frequency

	maxCount = max(mismatchCounter.values())
	return sorted([kmer for kmer, count in mismatchCounter.iteritems() if count == maxCount])

Text = "TGCGCACTTACAATTGATGCGCACTCTGACGTGGGTATTCGTCTGTATTCGTCTTACAATTGAAATAGATGTGAATAGATGTGCTGACGTGGAATAGATGTGTACAATTGATGCGCACTAATAGATGTGTACAATTGAGTATTCGTCTTACAATTGAAATAGATGTGGTATTCGTCTTACAATTGATGCGCACTCTGACGTGGTACAATTGATGCGCACTGTATTCGTCTAATAGATGTGGTATTCGTCTGTATTCGTCTAATAGATGTGCTGACGTGGCTGACGTGGTACAATTGAGTATTCGTCTGTATTCGTCTTGCGCACTTGCGCACTGTATTCGTCTAATAGATGTGGTATTCGTCTCTGACGTGGAATAGATGTGTGCGCACTGTATTCGTCTAATAGATGTGCTGACGTGGAATAGATGTGGTATTCGTCTCTGACGTGGTACAATTGATGCGCACTCTGACGTGGCTGACGTGGTGCGCACTGTATTCGTCTAATAGATGTGTACAATTGAAATAGATGTGCTGACGTGGAATAGATGTGTACAATTGAAATAGATGTGTACAATTGAGTATTCGTCTGTATTCGTCTGTATTCGTCTCTGACGTGGTGCGCACTAATAGATGTGTGCGCACTGTATTCGTCTTGCGCACTTGCGCACTTGCGCACTCTGACGTGGAATAGATGTGTGCGCACTCTGACGTGGAATAGATGTGAATAGATGTGTACAATTGATGCGCACTGTATTCGTCTTACAATTGAGTATTCGTCTTGCGCACTCTGACGTGGCTGACGTGGCTGACGTGGTGCGCACTCTGACGTGGCTGACGTGGGTATTCGTCTTACAATTGACTGACGTGGAATAGATGTGTACAATTGATACAATTGATACAATTGACTGACGTGGCTGACGTGGGTATTCGTCTGTATTCGTCTCTGACGTGGGTATTCGTCT"
k = 7
d = 2

mostFreqKmers = fWordsMismatch_and_RevComp(Text, k, d)
print ' '.join(mostFreqKmers)
