#Python 2.7.5 
codon_table = {
    "A": ["GCU", "GCC", "GCA", "GCG"],
    "C": ["UGU", "UGC"],
    "D": ["GAU", "GAC"],
    "E": ["GAA", "GAG"],
    "F": ["UUU", "UUC"],
    "G": ["GGU", "GGC", "GGA", "GGG"],
    "H": ["CAU", "CAC"],
    "I": ["AUU", "AUC", "AUA"],
    "K": ["AAA", "AAG"],
    "L": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
    "M": ["AUG",],
    "N": ["AAU", "AAC"],
    "P": ["CCU", "CCC", "CCA", "CCG"],
    "Q": ["CAA", "CAG"],
    "R": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
    "S": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
    "T": ["ACU", "ACC", "ACA", "ACG"],
    "V": ["GUU", "GUC", "GUA", "GUG"],
    "W": ["UGG",],
    "Y": ["UAU", "UAC"],
    "": ["UAA", "UAG", "UGA"],
}


def ProteinTranslation(Pattern):
    Protein =[]
    i=0
    while i < len(Pattern):
        Codon = Pattern[i:i+3]
        for j in codon_table:
            for k in codon_table[j]:
                if k==Codon:
                    Protein.append(j)
        i=i+3
        
    return "".join(Protein)


file_name = raw_input("Enter the file name: ")
try:
    file_handle = open(file_name)
except:
    print "File cannot be opened: ", file_name
    exit()

lines = file_handle.readlines()

pattern = lines[0].rstrip()

translation = ProteinTranslation(pattern)

output  = open("output.txt", "w")
output.write(translation)
output.close()
