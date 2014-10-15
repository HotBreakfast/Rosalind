def ReverseComplement(Pattern):
    reverse = list(Pattern[::-1])
    reverse_complement = reverse
    
    for i in range(0, len(reverse)):
        if reverse[i] == "A":
            reverse_complement[i] = "T"
        elif reverse[i] == "T":
            reverse_complement[i] = "A"
        elif reverse[i] == "C":
            reverse_complement[i] = "G"
        elif reverse[i] == "G":
            reverse_complement[i] = "C"

    return "".join(reverse_complement)
            
        

pattern = raw_input("Enter Pattern: ")
reverse_complement = ReverseComplement(pattern)

print  "Reverse complement: ", reverse_complement
