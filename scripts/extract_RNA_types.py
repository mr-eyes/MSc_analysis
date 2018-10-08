"""
Script purpose: extracting the RNA types from the transcripts files downloaded from refseq with the extension *.rna.fna
"""


import sys

if len(sys.argv) < 2:
    exit("Please pass the file name..")

file_name = sys.argv[1]


types = {}

with open(file_name, "r") as f:
    for line in f:
        if line[0] != ">":
            continue
        _type = line.split("|")[-2].replace("\n", "")
        if _type not in types:
            types[_type] = 1
        else:
            types[_type] = types[_type] + 1


print ("Found types are:")
for i in range(len(types.keys())):
    print ("%d- Type: %s | count: %d" %
           (i+1, types.keys()[i], types[types.keys()[i]]))
