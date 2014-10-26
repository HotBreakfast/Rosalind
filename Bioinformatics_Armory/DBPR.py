#Python 2.7.5
from Bio import ExPASy
from Bio import SwissProt
import re

def BiologicalProcesses(UniProtID):
    Handle = ExPASy.get_sprot_raw(UniProtID)
    Record = SwissProt.read(Handle)

    Processes = []
    for i in Record.cross_references:
        if "GO" in i:
            for j in i:
                if re.match("P:.*", j):
                    Processes.append(j[j.rfind(':')+1:])
    return "\n".join(Processes)


UniProtID = raw_input("Enter UniProt ID: ")
processes = BiologicalProcesses(UniProtID)

print processes
