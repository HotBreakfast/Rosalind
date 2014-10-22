#Python 2.7.5
def HammingDistance(Text1, Text2):
    hamming_distance=0
    for i in range(0, len(Text1)):
        if Text1[i] != Text2[i]:
            hamming_distance = hamming_distance + 1
    return hamming_distance



file_name = raw_input("Enter the file name: ")

try:
    file_handle = open(file_name)
except:
    print "File cannot be opened: ", file_name
    exit()

lines = file_handle.readlines()

string1 = lines[0].rstrip()
string2 = lines[1].rstrip()


hamming_distance = HammingDistance(string1, string2)

print "Hamming distance: ", hamming_distance
