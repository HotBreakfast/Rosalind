def PatternCount(Text, Pattern):
    count = 0

    for i in range(0, len(Text)-len(Pattern)):
        if Text[i: i + len(Pattern)] == Pattern:
            count = count+1

    return count

def FrequentWords(Text, k):
    FrequentPatterns = set()
    Count={}
    
    for i in range(0, len(Text)-k):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Text, Pattern)
        
    maxCount = max(Count.values())
    
    for i in range(0, len(Text)-k):
        if Count[i] == maxCount:
            FrequentPatterns.add(Text[i:i+k])

    FrequentPatterns = list(FrequentPatterns)
    FrequentPatterns.sort()
    
    return " ".join(FrequentPatterns)



text = raw_input("Enter Text: ")
k = int(raw_input("Enter k: "))
frequent_words = FrequentWords(text,k)


print  "Most frequent {}-mers: ".format(k), frequent_words
