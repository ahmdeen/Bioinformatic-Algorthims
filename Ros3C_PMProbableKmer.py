("""
Profile-most Probable Kmer Problem

"""


infile = open('rosalind_3c.txt', 'r')
Text = infile.readline().strip()
k = int(infile.readline().strip())

Profile = [map(float,line.strip().split()) for line in infile]
print Profile
#a, c, g, t = 

#for line in infile:
    #a, c, g, t = map(float, line.strip().split())
#Profile.append({'A':a,'C':c,'G':g,'T':t})
    
infile.close()

def PMProbableKmer(seq, k, Profile):

    NDict = {nucleotide:index for index, nucleotide in enumerate('ACGT') }
    #print NDict

    maxProb = -1
    lenSeq = len(seq)

    for i in xrange(lenSeq - k + 1):
        prob = 1
        #print list(enumerate(seq[i:i+k]))
        for j, nucleotide in enumerate(seq[i:i+k]):
            prob *= Profile[NDict[nucleotide]][j]

        if prob > maxProb:
            maxProb = prob
            mostProb = seq[i:i+k]

    return mostProb


answer = PMProbableKmer(Text, k, Profile)

with open('Ros3C_Answer', 'w') as outfile:
    outfile.write(answer)

