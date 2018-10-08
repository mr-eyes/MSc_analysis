import re
import sys
import tqdm
from networkx import all_simple_paths, connected_component_subgraphs, DiGraph, number_of_nodes, Graph, connected_components


gfa_file = ""
output = ""

if len(sys.argv) > 2:
    gfa_file = sys.argv[1]
    output = sys.argv[2]
else:
    exit(
        "Please pass the GFA and output files paths\nEx: python kmer_based_clustering.py [GFA] [output]")

clusters = []
node_transcripts = {}
edges = []

with open(gfa_file) as gtf:
    for line in gtf:
        if line[0] == "S":
            main = re.findall(re.compile("S\t+(\d+).{1,}S:+(\w+\.\d+)"), line)
            extra = re.findall(re.compile(",+(\w+\.\d+)"), line)
            node = int(main[0][0])
            node_transcripts[node] = [main[0][1]]
            if len(extra) > 0:
                node_transcripts[node] = node_transcripts[node] + (list(extra))

        elif line[0] == "L":
            for z in re.finditer(re.compile("(\d+)\t[+,-]\t(\d+)\t[+,-]"), line):
                node_1 = int(z.group(1))
                node_2 = int(z.group(2))
                edges.append((node_1, node_2))


G = Graph()
G.add_nodes_from(node_transcripts.keys())
G.add_edges_from(edges)

graphs = list(connected_components(G))
print "Done creating graphs"

for i in range(len(graphs)):
    cluster = graphs[i]
    component_transcripts = set()
    for node in cluster:
        transcripts = node_transcripts[node]
        for tr in transcripts:
            component_transcripts.add(tr)
    clusters.append(list(component_transcripts))

result = open(output, "w")
result.write("cluster_id\ttranscripts_ids\n")
for i in range(len(clusters)):
    result.write(str(i)+"\t"+",".join(clusters[i])+"\n")

result.close()
