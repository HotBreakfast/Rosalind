#Python 2.7.5
CODON_TABLE = {
    "A": ["GCT", "GCC", "GCA", "GCG"],
    "C": ["TGT", "TGC"],
    "D": ["GAT", "GAC"],
    "E": ["GAA", "GAG"],
    "F": ["TTT", "TTC"],
    "G": ["GGT", "GGC", "GGA", "GGG"],
    "H": ["CAT", "CAC"],
    "I": ["ATT", "ATC", "ATA"],    
    "K": ["AAA", "AAG"],
    "L": ["TTA", "TTG", "CTT", "CTC", "CTA", "CTG"],
    "M": ["ATG",],
    "N": ["AAT", "AAC"],
    "P": ["CCT", "CCC", "CCA", "CCG"],
    "Q": ["CAA", "CAG"],
    "R": ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"],
    "S": ["TCT", "TCC", "TCA", "TCG", "AGT", "AGC"],
    "T": ["ACT", "ACC", "ACA", "ACG"],
    "V": ["GTT", "GTC", "GTA", "GTG"],
    "W": ["TGG",],
    "Y": ["TAT", "TAC"],
    "*": ["TAA", "TAG", "TGA"],
}

def ProteinTranslation(Pattern):
    Protein =[]
    i=0
    while i < len(Pattern):
        Codon = Pattern[i:i+3]
        for j in CODON_TABLE:
            for k in CODON_TABLE[j]:
                if k==Codon:
                    Protein.append(j)
        i=i+3
        
    return "".join(Protein)


def ReverseComplement(Pattern):
    reverse = list(Pattern[::-1])
    reverse_complement = []
    
    for i in range(0, len(reverse)):
        if reverse[i] == "A":
            reverse_complement.append("T")
        elif reverse[i] == "T":
            reverse_complement.append("A")
        elif reverse[i] == "C":
            reverse_complement.append("G")
        elif reverse[i] == "G":
            reverse_complement.append("C")

    return "".join(reverse_complement)


def PeptideEncoding(Text, Peptide):
    Substrings = []
    for i in range(0, len(Text)-len(Peptide)*3+1):
        Pattern = Text[i:i+len(Peptide)*3]
        RC = ReverseComplement(Pattern)
        
        Translation = ProteinTranslation(Pattern)
        TranslationRC = ProteinTranslation(RC)
        
        if Translation == Peptide:
            Substrings.append(Pattern)
        if TranslationRC == Peptide:
            Substrings.append(Pattern)
            
    return "\n".join(Substrings)




file_name = raw_input("Enter the file name: ")
try:
    file_handle = open(file_name)
except:
    print "File cannot be opened: ", file_name
    exit()

lines = file_handle.readlines()

text = lines[0].rstrip()
peptide = lines[1].rstrip()

encoding = PeptideEncoding(text, peptide)

output  = open("output.txt", "w")
output.write(encoding)
output.close()
