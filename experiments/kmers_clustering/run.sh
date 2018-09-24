mkdir K$2_assessement
python filter_by_length.py $1 filtered_k$2_$1 $2
./kallisto index -i $2.idx filtered_k$2_$1 -k $2
./kallisto inspect $2.idx --gfa=$2.gfa
rm *idx
python kmer_based_clustering.py $2.gfa clusters_k$2.tsv
rm *gfa
python assess_by_gene.py filtered_k$2_$1 clusters_k$2.tsv k$2_clusters_assessment.tsv > k$2_summary.txt
rm filtered_k$2_$1
mv *.tsv K$2_assessement/
mv *summary* K$2_assessement/