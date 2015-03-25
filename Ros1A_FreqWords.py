"""
Frequent Words 

Find the most frequent k-mers in a string.

Given: A DNA string Text and an integer k.

Return: All most frequent k-mers in Text (in any order).



Algorithm:

* Iterate through intervals of Text of length(Kmer)
	- This checks for each individual kmer that can possibly show up in Text 
	- Make sure to not extend past end of (Text - k)
* Check for each kmer in kmer Dictionary(hash table)
	> If kmer is in the kmer Dictionary, increment it's frequency
	> If kmer is not in the kmer Dictionary, add it to it
* Go through the Dictionary and find the maximum of the values
* Create List of Kmers in the Kmer Dictionary that have the maximum Frequency
* Return List


Alternative Ideas:

* Create



"""


#Inputs and Variables---------------------------------------
#-----------------------------------------------------------

'''File Input'''
with open('Data/rosalind_m4.txt') as inputData:
	Text, k= [line.strip() for line in inputData.readlines()]
	k = int(k)

inputData.close()

#-----------------------------------------------------------

'''Variables'''

lenText = len(Text)

#Stores the Kmers as the Key and the Frequency as the Value
kmerDict = {}
#-----------------------------------------------------------

'''Computing Frequent Kmers'''

#Iterates through all possible starting positions for a kmer
for i in xrange (lenText - k + 1):
	#Define the Kmer
	kmer = Text[i:i+k] 
	
	#Check if Kmer is in the Dict, Increment Freq if it is, Add it if its not
	if kmer in kmerDict: 
		kmerDict[kmer] += 1
	else:
		kmerDict[kmer] = 1
	i = i + k + 1

#Find the Maximum Freq in the Dict
max_freq = max(kmerDict.values())
#print max_freq

#Answer is list of kmers with max frequency
answer = [kmer for kmer, freq in kmerDict.items() if freq == max_freq]

print(' '.join(answer))






