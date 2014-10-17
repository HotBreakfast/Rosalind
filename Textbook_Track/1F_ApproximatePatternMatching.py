#Python 2.7.5
def HammingDistance(Text1, Text2):
    hamming_distance=0
    for i in range(0, len(Text1)):
        if Text1[i] != Text2[i]:
            hamming_distance = hamming_distance + 1
    return hamming_distance

def ApproximatePatternMatching(Pattern, Text, d):
    positions = []
    for i in range(0, len(Text)-d-1):
        if Text[i: i + len(Pattern)] == Pattern:
            positions.append(i)
        else:
            hamming_distance = HammingDistance(Text[i: i + len(Pattern)], Pattern)
            if hamming_distance <=d:
                positions.append(i)
    return " ".join(map(str,positions))



file_name = raw_input("Enter the file name: ")
try:
    file_handle = open(file_name)
except:
    print "File cannot be opened: ", file_name
    exit()

lines = file_handle.readlines()

pattern = lines[0].rstrip()
text = lines[1].rstrip()
d = int(lines[2])

starting_positions = ApproximatePatternMatching(pattern, text, d)

output  = open("output.txt", "w")
output.write(starting_positions)
output.close()
