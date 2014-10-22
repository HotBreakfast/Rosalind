#Python 2.7.5
AA_MASS = {
    "A": 71,
    "C": 103,
    "D": 115,
    "E": 129,
    "F": 147,
    "G": 57,
    "H": 137,
    "I": 113,    
    "K": 128,
    "L": 113,
    "M": 131,
    "N": 114,
    "P": 97,
    "Q": 128,
    "R": 156,
    "S": 87,
    "T": 101,
    "V": 99,
    "W": 186,
    "Y": 163
}

def CyclicSpectrum(Peptide):
    PrefixMass={}
    PrefixMass[0]=0
    for i in range(1, len(Peptide)+1):
        for j in AA_MASS:
            if Peptide[i-1] == j:
                PrefixMass[i]=PrefixMass[i-1]+AA_MASS[j]

    peptideMass = PrefixMass[len(Peptide)]

    CyclicSpectrum = [0]
    for i in range(0, len(Peptide)):
        for j in range(i+1, len(Peptide)+1):
            CyclicSpectrum.append(PrefixMass[j]-PrefixMass[i])
            if i > 0 and j < len(Peptide):
                CyclicSpectrum.append(peptideMass - (PrefixMass[j]-PrefixMass[i]))

    CyclicSpectrum = map(int,CyclicSpectrum)
    CyclicSpectrum.sort()
    
    return " ".join(map(str, CyclicSpectrum))



file_name = raw_input("Enter the file name: ")
try:
    file_handle = open(file_name)
except:
    print "File cannot be opened: ", file_name
    exit()
lines = file_handle.readlines()
peptide = lines[0].rstrip()
cyclic_spectrum = CyclicSpectrum(peptide)
output  = open("output.txt", "w")
output.write(cyclic_spectrum)
output.close()

