import tqdm
import re
import sys

def transcripts_to_loci(transcipts_ids):
    loci = {} # {locus:counted}
    for transcript in transcipts_ids:
        locus = transcript_locus[transcript]
        
        if locus in loci:
            loci[locus] += 1
        else:
            loci[locus] = 1
    
    return loci


def transcripts_to_genes(transcipts_ids):
    genes = {} # {locus:counted}
    for transcript in transcipts_ids:
        gene = transcript_gene[transcript]
        
        if gene in genes:
            genes[gene] += 1
        else:
            genes[gene] = 1
    
    return genes

def how_many_loci(cluster):
    return len(transcripts_to_loci(cluster))

def how_many_complete_loci(cluster):
    loci = transcripts_to_loci(cluster)
    complete = 0
    for key, value in loci.iteritems():
        if len(locus_transcripts[key]) == value:
            complete += 1
    
    return complete

def Q1(cluster):
    cluster_loci = transcripts_to_loci(cluster)
    for key, value in cluster_loci.iteritems():
        if len(locus_transcripts[key]) != value:
            return False
    
    return True


def Q2(cluster):
    if len(transcripts_to_genes(cluster)) > 1:
        return True
    else:
        return False


fasta_file_path = ""
clstr_file_path = ""


if len(sys.argv) < 3:
    sys.exit("Kindly pass positional arguments, ex: python clusters_assessment.py [fasta_file] [clstr_file]")

else:
    fasta_file_path = sys.argv[1]
    clstr_file_path = sys.argv[2]


tt = 0
tf = 0
ft = 0
ff = 0


locus_transcripts = {} # locus_0 : gene1,gene2,...
transcript_locus = {}  # gene1:locus1, gene2:locus1, gene3:locus3

gene_transcripts = {}  # gene_id: transcript1,transcript2,.....
transcript_gene = {}   # transcript1: gene9, transcript2: gene1, ....


with open(fasta_file_path) as fa:
    for line in fa:
        if line[0] != ">":
            continue
        fields = line.split("|")
        transcript_id = fields[0][1:]
        gene = fields[1]
        locus = fields[-2]
        transcript_locus[transcript_id] = locus
        transcript_gene[transcript_id] = gene

        if gene in gene_transcripts:
            gene_transcripts[gene].append(transcript_id)
        else:
            gene_transcripts[gene] = [transcript_id]

        if locus in locus_transcripts:
            locus_transcripts[locus].append(transcript_id)
        else:
            locus_transcripts[locus] = [transcript_id]



clstr_file = open(clstr_file_path, "r")
clstr_data = clstr_file.read()
clstr_file.close()

rep = {"\t": ",", "at +/": "", "at -/": "", "...": ",", "nt": "", "%": "", " ": ""}
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
res.write("cluster_id\tQ1\tQ2\tNo. loci\t No. Complete Loci\n")

for cluster_id, transcripts_ids in sorted(clusters_transcripts_ids.iteritems()):
    q1 = Q1(transcripts_ids)
    q2 = Q2(transcripts_ids)
    no_loci = how_many_loci(transcripts_ids)
    no_complete_loci = how_many_complete_loci(transcripts_ids)
    
    ans1 = ""
    ans2 = ""

    if q1 == True and q2 == True:
        ans1, ans2 = "Complete", "Mixed"
        tt += 1
    if q1 == True and q2 == False:
        ans1, ans2 = "Complete", "Clean"
        tf += 1
    if q1 == False and q2 == True:
        ans1, ans2 = "InComplete", "Mixed"
        ft += 1
    if q1 == False and q2 == False:
        ans1, ans2 = "InComplete", "Clean"
        ff += 1


    line = str(cluster_id) + "\t" + ans1 + "\t" + ans2 + "\t" + str(no_loci) + "\t" + str(no_complete_loci) + "\n"
    res.write(line)

res.close()


print ("%d Complete Mixed Components | [TT]\n") % (tt)
print ("%d Complete Clean Components | [FT]\n") % (tf)
print ("%d Incomplete Mixed  Components | [FT]\n") % (ft)
print ("%d Incomplete Clean Components | [FF]\n") % (ff)