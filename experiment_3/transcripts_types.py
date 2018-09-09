import sys

f_name = ""

if len(sys.argv) > 2:
    exit("pass the file name, python transcripts_types.py [file_name]")
else:
    f_name = sys.argv[1]

types = {}
with open(f_name,"r") as tr:
    for line in tr:
        if line[0] == ">":
            _type = line.split("|")[-2]
            if _type in types:
                types[_type] += 1
            else:
                types[_type] = 1

total = 0
count = 1

for key,val in types.iteritems():
    total += val
    print "%d-%s: %d" % (count, key, val)
    count += 1

print "_" * 80
print "Total: ", total