#Python 2.7.5

import itertools
def Permutations(k):
    seq="ATCG"
    permutations = []
    for p in itertools.product(seq, repeat=k):
        permutations.append("".join(p))
    return permutations


def HammingDistance(Text1, Text2):
    hamming_distance=0
    for i in range(0, len(Text1)):
        if Text1[i] != Text2[i]:
            hamming_distance = hamming_distance + 1
    return hamming_distance


def ApproximatePatternCount(Text, Pattern, d):
    count = 0
    for i in range(0, len(Text)-len(Pattern)+d-1):
        if HammingDistance(Text[i: i + len(Pattern)], Pattern) <= d:
            count = count+1
    return count

     
def FrequentWordsMismatches(Text, k, d):
    FrequentPatterns = []
    Count={}
   
    permutations = Permutations(k)
    
    for i in range(0, len(permutations)):
        Count[i] = ApproximatePatternCount(Text, permutations[i], d)

    maxCount = max(Count.values())

    for i in range(0, len(Count)):
        if Count[i] == maxCount:
            FrequentPatterns.append(permutations[i])
            
    return " ".join(FrequentPatterns[::-1])


#Works for following example, but way too slow for larger cases
text ="CAGTCGCCATTCGTCGGCATCGCAGGTACAGCAGTCGTCGGTACCATCCATCCATCCATTCGCCATGTAGCAGCAGTACCATCCATCCATTCGCCATCCATCCATGTAGTACAGCCATTCGCAGGTAGTAGCACCATCAGGCATCGGCAGCATCGGTAGCATCGCAGTCGGCACCATGTACCATCCATGCAGCATCGCAGCCATCCATTCGGTATCGCAGCAGTCGCCATCCATTCGGCACAGTCGTCGGTACCATTCGGTAGTACAGGTAGCACAGGTACAGGTACCATGCACCATCCATCCATGTACCATGCACCATCCATCAGTCGGCACAGGTACCATGCAGCATCGCAGTCG"
k=8
d=2

print FrequentWordsMismatches(text, k, d)
