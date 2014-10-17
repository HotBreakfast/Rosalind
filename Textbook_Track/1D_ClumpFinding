#Python 2.7.5
def PatternCount(Text, Pattern):
    count = 0

    for i in range(0, len(Text)-len(Pattern)):
        if Text[i: i + len(Pattern)] == Pattern:
            count = count+1

    return count


def FrequentWords(Text, k, t):
    FrequentPatterns = set()
    Count={}
    
    for i in range(0, len(Text)-k):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Text, Pattern)
        
    minCount = t
    
    for i in range(0, len(Text)-k):
        if Count[i] >= minCount:
            FrequentPatterns.add(Text[i:i+k])

    FrequentPatterns = list(FrequentPatterns)
    
    return FrequentPatterns


def ClumpFinding(Genome, k, L, t):
    for i in range(0, L-k):
        return " ".join(FrequentWords(Genome, k, t))


genome = raw_input("Enter Genome: ")
k = int(raw_input("Enter k: "))
L = int(raw_input("Enter L: "))
t= int(raw_input("Enter t: "))

clumps = ClumpFinding(genome, k, L, t)

print "Clumps: ", clumps
