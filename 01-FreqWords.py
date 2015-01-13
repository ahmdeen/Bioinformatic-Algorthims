"""
Frequent Words 

Find the most frequent k-mers in a string.

Given: A DNA string Text and an integer k.

Return: All most frequent k-mers in Text (in any order).

"""


#Inputs ---------------------------------------------------
#----------------------------------------------------------
Text = raw_input()
k = int(raw_input())
#----------------------------------------------------------

#Variables-------------------------------------------------

length = len(Text)

d = {}

#-----------------------------------------------------------
for i in range (length - k + 1):
	kmer = Text[i:i+k]
	if kmer in d:
		d[kmer] += 1
	else:
		d[kmer] = 1

max_freq = max(d.values())

print max_freq
answer = [kmer for kmer, freq in d.items() if freq == max_freq]
#print answer
print(' '.join(answer))





