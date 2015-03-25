dna = [
'GGCGCCCTCTAGCATCACCGCTAGG',
'TTTCTGACATGAGTACCCAAGTAGG',
'TGAACTAGTTTACATGAATAGCAGA',
'AATCGGTGAGGGTTGAACATAGGAG',
'CCCGGTTCATAATAGGAGTTAATGG',
'TTTCCCAGAGACGTCTCCATTTACC',
'CGAGGATCATTCGTCACTATAATCC',
'GAGTTTCCCATAGTGGTCATTGGTT',
'AATTTACTAGTAGGCTAGCCTGCAT',
'GGCATCGCCGACTTCTGAACTTACT']
k = int(raw_input())
d = int(raw_input()) 


def snp (seq):
    basepairs = {'A':['C','T','G'],'C':['A','T','G'],'T':['A','C','G'],'G':['A','C','T']}
    k = len(seq)
    listseq = [seq]
    for i in range(k):
        for j in basepairs[seq[i]]:
            listseq.append(seq[0:i] + j + seq[i+1:])
    return listseq
 
   
def tnp(seq, k):
    npSet = set()            
    for i in range( 0, len(seq) - k +1):
        kmer = seq[i:i+k]
        for snp in snp(kmer):
            npSet.add(snp)
    return list(npSet)
    
def iterator(seq1, seq2):
    compList = 0
    for i in range (0, len(seq1)):
        if seq1[i] != seq2[i]:
            compList += 1
    return compList

def motifEnum(dna, k, d):
    holder = set()
    length = len(dna[0])
    for i in range(0, length - k +1): 
        a = dna[0][i:i+k] #for each kmer a in Dna
        realNP = set()
        for poly in snp(a): 
            for poly2 in snp(poly):
                realNP.add(poly2)
        for aprime in list(realNP):
            foundcounter = 0
            for d in dna:
                for i in range(0, len(d) - k +1):
                    sub = d[i:i+k]
                    if iterator(aprime,sub) <= 2:
                        foundcounter += 1
                        break
            if foundcounter == len(dna):
                holder.add(aprime)
    return sorted(list(holder))    

answer = motifEnum(dna, k, d)
#outfile = open('answer.txt', 'w')
print (' '.join(map(str,answer)))
#outfile.close()