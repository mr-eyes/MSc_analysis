import sys
import re
import tqdm
import gc


if len(sys.argv) == 1:
    exit("Please pass .clstr file path as sys.arg ")

clstr_file_path = sys.argv[1]


clstr_file = open(clstr_file_path, "r")
clstr_data = clstr_file.read()
clstr_file.close()

rep = {"\t": ",", "at +/": "", "at -/": "", "...": ",", "nt": "", "%": "", " ": ""}
rep = dict((re.escape(k), v) for k, v in rep.iteritems())
pattern = re.compile("|".join(rep.keys()))
clstr_data = pattern.sub(lambda m: rep[re.escape(m.group(0))], clstr_data)

gc.collect()

tsv = open("cdhit_stats.tsv","w")
tsv.write("\t".join(["cluster_id", "total_seq_count", "rep_seq", "all_seq", "total_length (nt)", "avg_similarity (%)"]) + "\n")
all_clusters = clstr_data.split(">Cluster")
largest_cluster_id = 0
seq_count_largest_cluster = 0

for i in tqdm.tqdm(range(1, len(all_clusters), 1)):
    cluster = all_clusters[i]
    cluster = cluster.split("\n")
    cluster_id = cluster[0]
    total_seq_count = 0
    rep_seq = ""
    all_seq = []
    total_length_nt = 0
    similarity = 0.0
    avg_similarity = 0.0
    for item in cluster[1:-1]:
        item = item.replace(">","").split(",")
        seq_id = item[0]
        seq_length = int(item[1])
        seq_acc = item[2]
        seq_cov = item[3]
        all_seq.append(seq_acc)
        total_length_nt += seq_length
        if "*" in seq_cov:
            rep_seq = seq_acc
        else:
            similarity += float(seq_cov)

        total_seq_count += 1
    
    all_seq = ",".join(all_seq)
    avg_similarity = similarity / total_seq_count
    tsv_line = "%s\t%d\t%s\t%s\t%d\t%.2f" % (cluster_id, total_seq_count, rep_seq, all_seq, total_length_nt, avg_similarity)
    if total_seq_count > seq_count_largest_cluster:
        largest_cluster_id = cluster_id
        seq_count_largest_cluster = total_seq_count

    #print tsv_line
    tsv.write(tsv_line + "\n")    
         
tsv.close()

print "Largest Cluster ID: %s has %d Sequences." % (largest_cluster_id, seq_count_largest_cluster)
