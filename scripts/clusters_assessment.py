import tqdm
import re

def transcripts_to_loci(transcipts_ids):
    loci = {} # {locus:counted}
    for transcript in transcipts_ids:
        locus = transcript_locus[transcript]
        
        if locus in loci:
            loci[locus] += 1
        else:
            loci[locus] = 1
    
    return loci


def Q1(cluster):
    cluster_loci = transcripts_to_loci(cluster)
    for key, value in cluster_loci.iteritems():
        if len(locus_transcripts[key]) != value:
            return False
    
    return True


def Q2(cluster):
    if len(transcripts_to_loci(cluster)) > 1:
        return True
    else:
        return False


tt = 0
tf = 0
ft = 0
ff = 0


locus_transcripts = {} # locus_0 : gene1,gene2,...
transcript_locus = {}  # gene1:locus1, gene2:locus1, gene3:locus3

with open("loci.fa") as fa:
    for line in fa:
        if line[0] != ">":
            continue
        fields = line.split("|")
        transcript_id = fields[0][1:]
        locus = fields[-2]
        transcript_locus[transcript_id] = locus
        if locus in locus_transcripts:
            locus_transcripts[locus].append(transcript_id)
        else:
            locus_transcripts[locus] = [transcript_id]


clstr_file_path = "85.clstr"


clstr_file = open(clstr_file_path, "r")
clstr_data = clstr_file.read()
clstr_file.close()

rep = {"\t": ",", "at +/": "", "at -/": "",
       "...": ",", "nt": "", "%": "", " ": ""}
rep = dict((re.escape(k), v) for k, v in rep.iteritems())
pattern = re.compile("|".join(rep.keys()))
clstr_data = pattern.sub(lambda m: rep[re.escape(m.group(0))], clstr_data)
all_clusters = clstr_data.split(">Cluster")

clusters_transcripts_ids = {}

for i in tqdm.tqdm(range(1, len(all_clusters), 1)):
    cluster = all_clusters[i]
    cluster = cluster.split("\n")
    cluster_id = int(cluster[0])

    for item in cluster[1:-1]:
        item = item.replace(">", "").split(",")
        transcript_id = item[2].split("|")[0]

        if cluster_id in clusters_transcripts_ids:
            clusters_transcripts_ids[cluster_id].append(transcript_id)

        else:
            clusters_transcripts_ids[cluster_id] = [transcript_id]


res = open("result.tsv", "w")
res.write("cluster_id\tQ1\tQ2\n")

for cluster_id, genes_ids in sorted(clusters_transcripts_ids.iteritems()):
    q1 = Q1(genes_ids)
    q2 = Q2(genes_ids)
    line = str(cluster_id) + "\t" + str(q1) + "\t" + str(q2) + "\n"
    res.write(line)

    if q1 == True and q2 == True:
        tt += 1
    if q1 == True and q2 == False:
        tf += 1
    if q1 == False and q2 == True:
        ft += 1
    if q1 == False and q2 == False:
        ff += 1


res.close()


print ("%d Clusters has All isoforms came from the same gene and there are missing isoforms grouped in other components. (high threshold problem | [TT])\n") % (tt)
print ("%d Clusters has All isoforms came from the same gene and there are no other isoforms grouped in other components. (perfect component) | [FT]\n") % (tf)
print ("%d Clusters has Mixed isoforms from multiple genes and some isoforms grouped in other components | [FT].\n") % (ft)
print ("%d Clusters has Mixed isoforms from multiple genes and there are no related isoforms in other components. (Low threshold problem) | [FF]\n") % (ff)
