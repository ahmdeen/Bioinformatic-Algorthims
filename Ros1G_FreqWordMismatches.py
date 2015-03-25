import sys



"""
Frequent Words with Mismatches Problem

Find the most frequent k-mers with mismatches in a string.

Given: A string Text as well as integers k and d.

Return: All most frequent k-mers with up to d mismatches in Text.

Sample Dataset

"""

from collections import defaultdict
from itertools import combinations, product, izip

def freqWordMismatcher(Text, k, d):
	'''Returns all most frequent kmers with at most d mismatches in Text'''
	lenText = len(Text)

	##Generate Kmer Frequencies for all Kmers in Text
		#Prevents generating mismatches for the same Kmer Twice 
	kmerFreq = defaultdict(int)
	for i in xrange(lenText - k + 1):
		kmerFreq[Text[i:i+k]] +=1

	##Grabs all the mismatch kmers for every unique kmer in Text that appears with its particular frequency
	mismatchCounter = defaultdict(int) #dictionary of mismatches to the kmers in kmerFreq
	for kmer, frequency in kmerFreq.iteritems(): 
		for mismatch in kmerMismatcher(kmer,d): 
			mismatchCounter[mismatch] += frequency

	#Find the mismatch kmers that has the maximum frequency of the most frequent kmer
	maxCount = max(mismatchCounter.values())
	return sorted([kmer for kmer, count in mismatchCounter.iteritems() if count == maxCount])

def kmerMismatcher(kmer, d):
	'''Returns all mismatched kmers that have at most d mismatches with given kmer'''
	
	
	mismatches = [kmer]#Initialize Mismatches with given Kmer

	k = len(kmer)

	#Dictionary of all Possible Alternate Bases
	baseAlts = {'A':'CGT', 'C':'AGT', 'G':'ACT', 'T':'ACG'}

	#For each number of mismatches up to d
	for distance in xrange(1, d + 1):

		#For every index in kmer, generate possible positions for mismatches
		for changeIndices in combinations(xrange(k), distance): 
			#Create possible subsitutions for each generated mismatch position in Kmer
			for subs in product(*[baseAlts[kmer[i]] for i in changeIndices]):
				
				newMismatch = list(kmer)

				#For every mismatch index and current subsitution base, subsitute into mismatch kmer string
				for index, sub in izip(changeIndices, subs):
					newMismatch[index] = sub
				mismatches.append(''.join(newMismatch))
	return mismatches




Text = "TCTATTAATCTATTAATCTATTAAATTTGCTAGTCTATTAACCAAAATCCCACGACAGTCACGACAGTCACGACAGTCACGACAGTTCGCAGCTCTCGCAGCTCCCAAAATCCTCGCAGCTCTCGCAGCTCTCGCAGCTCATTTGCTAGCCAAAATCCTCGCAGCTCATTTGCTAGTCGCAGCTCCACGACAGTATTTGCTAGTCGCAGCTCTCGCAGCTCCACGACAGTCCAAAATCCCACGACAGTCACGACAGTATTTGCTAGCACGACAGTATTTGCTAGTCGCAGCTCATTTGCTAGTCGCAGCTCCACGACAGTTCGCAGCTCCCAAAATCCTCGCAGCTCTCTATTAAATTTGCTAGCCAAAATCCATTTGCTAGTCTATTAACCAAAATCCCACGACAGTCACGACAGTCCAAAATCCCACGACAGTCACGACAGTTCTATTAACCAAAATCCTCGCAGCTCTCGCAGCTCCCAAAATCCCACGACAGTATTTGCTAGTCTATTAACCAAAATCCATTTGCTAGTCGCAGCTCTCTATTAATCGCAGCTCTCGCAGCTCCCAAAATCCCACGACAGTATTTGCTAGTCTATTAATCGCAGCTCATTTGCTAGTCGCAGCTCCCAAAATCCCACGACAGTTCGCAGCTCCACGACAGTATTTGCTAGATTTGCTAGCACGACAGTTCTATTAAATTTGCTAGTCTATTAATCGCAGCTCCCAAAATCCCACGACAGTTCTATTAATCTATTAATCGCAGCTCTCGCAGCTCCACGACAGTATTTGCTAGCACGACAGTCACGACAGTCCAAAATCCATTTGCTAGTCTATTAAATTTGCTAGTCTATTAACACGACAGT"
k = 7
d = 3

mostFreqKmers = freqWordMismatcher(Text, k, d)

print ' '.join(mostFreqKmers)
