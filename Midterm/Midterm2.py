


from itertools import product
from operator import ne 

def HammDist(seq1, seq2):
    if len(seq1) != len(seq2):
        raise ValueError('Sequences are not equal length')
    
    #sums together a comparison of each of the basepairs 
    #maps the function to each of the characters in seq1 and seq2
    #(Ne returns true if different characters, sum will count the amount of true statements)
    return sum(map(ne, seq1, seq2)) 


def median_string(k, dna_list):
    
    best_score = k*len(dna_list) + 1

    for pattern in product('ACGT', repeat=k):
        current_score = sum([motif_score(''.join(pattern), dna) for dna in dna_list]) + max([motif_score(''.join(pattern), dna) for dna in dna_list])
        if current_score < best_score:
            best_score = current_score
            best_pattern = ''.join(pattern)

    return best_pattern


def motif_score(pattern, motif):
    '''Returns the score of d(pattern, motif).'''
    #print len(motif[0:0+len(pattern)]), len(pattern)
    return min([HammDist(motif[i:i+len(pattern)], pattern) for i in range(len(motif)-len(pattern)+1)])




# Read the input data.
with open('rosalind_m5.txt') as input_data:
    k = int(input_data.readline())
    dna_list = [line.strip() for line in input_data.readlines()]

# Get the best pattern.
best_pattern = median_string(k, dna_list)

# Print and save the answer.
print best_pattern
with open('Answer2.txt', 'w') as output_data:
        output_data.write(best_pattern)
