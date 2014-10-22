#Python 2.7.5
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
            
        

pattern = raw_input("Enter Pattern: ")
reverse_complement = ReverseComplement(pattern)

print  "Reverse complement: ", reverse_complement
