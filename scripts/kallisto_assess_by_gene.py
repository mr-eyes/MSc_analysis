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


def how_many_genes(cluster):
    return len(transcripts_to_genes(cluster))

def how_many_complete_loci(cluster):
    loci = transcripts_to_loci(cluster)
    complete = 0
    for key, value in loci.iteritems():
        if len(locus_transcripts[key]) == value:
            complete += 1
    
    return complete


def how_many_complete_genes(cluster):
    genes = transcripts_to_genes(cluster)
    complete = 0
    for key, value in genes.iteritems():
        if len(gene_transcripts[key]) == value:
            complete += 1

    return complete


def Q1(cluster):
    cluster_genes = transcripts_to_genes(cluster)
    for key, value in cluster_genes.iteritems():
        if len(gene_transcripts[key]) != value:
            return False
    
    return True


def Q2(cluster):
    if len(transcripts_to_loci(cluster)) > 1:
        return True
    else:
        return False


fasta_file_path = ""
clstr_file_path = ""
output_file = ""

if len(sys.argv) < 3:
    sys.exit(
        "Kindly pass positional arguments, ex: python clusters_assessment.py [fasta_file] [clstr_file] [output_file]")

else:
    fasta_file_path = sys.argv[1]
    clstr_file_path = sys.argv[2]
    output_file = sys.argv[3]


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


clusters_transcripts_ids = {}

with open(clstr_file_path, "r") as clusters:
    next(clusters)
    for line in clusters:
        fields = line.split("\t")
        cluster_id = int(fields[0])
        _transcripts = fields[1].split(",")
        transcripts = []
        for tr in _transcripts:
            transcripts.append(tr.replace("\n", ""))

        clusters_transcripts_ids[cluster_id] = transcripts

res = open(output_file, "w")
res.write("cluster_id\tQ1\tQ2\tloci\tcomplete_loci\tgenes\tcomplete_genes\n")

for cluster_id, transcripts_ids in sorted(clusters_transcripts_ids.iteritems()):
    q1 = Q1(transcripts_ids)
    q2 = Q2(transcripts_ids)
    no_loci = how_many_loci(transcripts_ids)
    no_genes = how_many_genes(transcripts_ids)
    no_complete_loci = how_many_complete_loci(transcripts_ids)
    no_complete_genes = how_many_complete_genes(transcripts_ids)

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

    line = str(cluster_id) + "\t" + ans1 + "\t" + ans2 + "\t" + str(no_loci) + "\t" + str(no_complete_loci) + "\t" + str(no_genes) + "\t" + str(no_complete_genes) + "\n"
    res.write(line)

res.close()


print ("%d Complete Mixed Components | [TT]\n") % (tt)
print ("%d Complete Clean Components | [FT]\n") % (tf)
print ("%d Incomplete Mixed  Components | [FT]\n") % (ft)
print ("%d Incomplete Clean Components | [FF]\n") % (ff)
