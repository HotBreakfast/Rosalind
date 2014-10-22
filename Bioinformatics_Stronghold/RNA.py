#Python 2.7.5 
def Transcription(DNA):
    RNA = []
    for nucleotide in DNA:
        if nucleotide == "T":
            RNA.append("U")
        else:
            RNA.append(nucleotide)
           
    return "".join(RNA)

dna = raw_input("Enter DNA: ")
print "RNA: ", Transcription(dna)
