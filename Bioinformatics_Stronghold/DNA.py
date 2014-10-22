#Python 2.7.5
def CountNucleotides(DNA):
    CountA=0
    CountT=0
    CountC=0
    CountG=0
    
    for nucleotide in DNA:
        if nucleotide == "A":
            CountA=CountA+1
        elif nucleotide == "T":
            CountT=CountT+1
        elif nucleotide == "C":
            CountC=CountC+1
        elif nucleotide == "G":
            CountG=CountG+1
            
    return " ".join(map(str,[CountA, CountC, CountG, CountT]))

text = raw_input("Enter Text: ")
print CountNucleotides(text)
