import sys
"""
Median String Problem
"""
basepairs = ['A', 'C','G','T']

#hardcode dna collection of strings
dna = ['AGTGCACCTCAGGTTCACCGCATTTGCTAGCACCTTCGTGAT',
'AGAAACCATTGTGCATTAGCACTACTCAATAGCGCATAATAA',
'TGAGATAGTGCAACATACAGGCCCTCGCGCGGTCAGGTAACC',
'CATCGGAGTGCATTTATAATAAAAAGTCAACAGCGGATAACT',
'CAGGGATCTTACCACTATAGGGCATGCAGTCACGAGGCATAG',
'ATGAGGTGAAGGAGGGCACTGGGGGGGGGTAAACTAGAGCGG',
'AGTGCACTCCCGCACCGCTCCGTGGAGAACCTACTATTCCTG',
'ATCCCCCAACTCAGAGCAGCTTGCGGTTCCGTAGCCTCTTGA',
'GATCTGAAACTCAGTGCACCATACAATCTGATTCTAGTTATG',
'ACCTAGGCTCGAAAGACCATCTAGAGTGCAGAATCCCCGCCA',]  
k = int(raw_input()) 


def kmerGen(k): 
    bases = basepairs 
    if k == 1:
        return bases
    else:
        new = []
        for i in kmerGen(k-1):
            for j in bases:
                new.append(i + j)
        return new

def di(seq1, seq2):
    diffCounter = 0
    for i in range(0,len(seq1)):
        if seq1[i] != seq2[i]:
            diffCounter +=1
    return diffCounter

def d(pattern, seq):
    dist = 0
    pLen = len(pattern)
    
    #for every string in dna 
    for s in seq:
        minVal = di(pattern, s[0:pLen])
        for i in range (0, len(s) - pLen + 1):
            kmer = s[i:i + pLen]
            minVal = min(minVal, di(pattern, kmer))
        dist += minVal
    return dist

def medString(dna,k):
    kList = sorted(kmerGen(k))
    medStr = kList[0]
    dbest = sys.maxint
    for pattern in kList:
        dnow = d(pattern, dna)
        if (dnow < dbest):
            medStr = pattern
            dbest = dnow
    return medStr

print medString(dna, k)