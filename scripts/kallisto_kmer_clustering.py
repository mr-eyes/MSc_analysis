import re
import sys
from networkx import Graph, connected_components

clusters = []
node_transcripts = {}
edges = []

gfa_file = ""

if len(sys.argv) > 1:
    gfa_file = sys.argv[1]
else:
    exit("Please pass the GFA file path.")


with open(gfa_file) as gtf:
    for line in gtf:
        if line[0] == "S":
            main = re.findall(re.compile("S\t+(\d+).{1,}S:+(\w+\.\d)"), line)
            extra = re.findall(re.compile(",+(\w+\.\d)"), line)
            node = int(main[0][0])
            node_transcripts[node] = [main[0][1]]
            if len(extra) > 0:
                node_transcripts[node] =  node_transcripts[node] + (list(extra))
            
        elif line[0] == "L":
            for z in re.finditer(re.compile("(\d+)\t[+,-]\t(\d+)\t[+,-]"), line):
                node_1 = int(z.group(1))
                node_2 = int(z.group(2))
                edges.append((node_1, node_2))
                
            
G = Graph()
G.add_nodes_from(node_transcripts.keys())
G.add_edges_from(edges)   

for cluster in connected_components(G):
    for node in cluster:
        clusters.append(node_transcripts[node])

result = open("clusters.tsv","w")
result.write("cluster_id\ttranscripts_ids\n")
for i in range(len(clusters)):
    result.write(str(i)+"\t"+",".join(clusters[i]))

result.close()
