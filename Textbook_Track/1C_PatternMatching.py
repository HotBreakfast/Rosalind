def StartingPositions(Pattern, Genome):
    positions = []
    for i in range(0, len(Genome)-len(Pattern)):
        if Genome[i: i + len(Pattern)] == Pattern:
            positions.append(i)
    return " ".join(map(str,positions))


pattern = raw_input("Enter Pattern: ")
genome = raw_input("Enter Genome: ")       
starting_positions = StartingPositions(pattern, genome)

print "Starting positions: ", starting_positions
