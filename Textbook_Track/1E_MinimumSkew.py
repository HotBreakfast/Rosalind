##Python 2.7.5
def MinimumSkew(Genome):
    Skew=0
    skew_values = [0]
    for i in range(0, len(Genome)):
        if Genome[i] == "G":
            Skew=Skew+1
        elif Genome[i] == "C":
            Skew=Skew-1
        elif Genome[i] == "A" or "T":
            Skew=Skew
            
        skew_values.append(Skew)
        
    minSkew = min(skew_values)
    minSkew_positions = []
    for i in range(0, len(skew_values)):
        if skew_values[i]== minSkew:
            minSkew_positions.append(i)
        
    return " ".join(map(str,minSkew_positions))



file_name = raw_input("Enter the file name: ")
try:
    file_handle = open(file_name)
except:
    print "File cannot be opened: ", file_name
    exit()

lines = file_handle.readlines()

genome = lines[0]
position_minimum_skew = MinimumSkew(genome)

print  "Positions minimizing the skew: ", position_minimum_skew
