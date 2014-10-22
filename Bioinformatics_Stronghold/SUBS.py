#Python 2.7.5
def PatternMatching(Pattern, Genome):
    positions = []
    for i in range(0, len(Genome)-len(Pattern)):
        if Genome[i: i + len(Pattern)] == Pattern:
            positions.append(i+1)
    return " ".join(map(str,positions))



genome = raw_input("Enter Genome: ")
pattern = raw_input("Enter Pattern: ")      
starting_positions = PatternMatching(pattern, genome)

print "Starting positions: ", starting_positions
