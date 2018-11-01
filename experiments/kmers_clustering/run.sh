#!/bin/bash

ASSESS=../../scripts/kCluster_assess_by_gene.py
KPROCESSOR=kProcessor/Kprocessor
FASTA=$(sed "s/.*\///" <<< $1)
KMER=$2
TYPE=$3

# Generating kProcessor index
echo "Generating index for kmer size: ${KMER}"
#./${KPROCESSOR} index -i min_$FASTA --names min_$FASTA.names --method MAP -k ${KMER} -o ${TYPE}_k${KMER}_index

# Generate kCluster Relations File
#python kCluster/scripts/generate_relations.py ${TYPE}_k${KMER}_index.map ${TYPE}_${KMER}_index.namesMap min_$FASTA ${KMER} ${TYPE}_k${KMER}_relations


# Perform Clustering of kCluster Relations File (Thresholds 1:100 %)
for THRESHOLD in {0..100..1};
do pypy kCluster/scripts/relations_clustering.py ${TYPE}_k${KMER}_relations.tsv ${TYPE}_k${KMER}_index.namesMap $THRESHOLD;
done

# # Delete the original index file
# rm ${TYPE}_${KMER}_index.map

# Perform Clustering Assessment and save output files
for THRESHOLD in {0..100..1};
do pypy $ASSESS $1 clusters_c${THRESHOLD}.0_${TYPE}_k${KMER}_index.tsv kCluster_k${KMER}_${THRESHOLD}_assessment.tsv;
done


mkdir -p ${TYPE}/k${KMER}/{clusters,stats,summaries,details,visualization}
mv *txt ${TYPE}/k${KMER}/summaries
mv *json ${TYPE}/k${KMER}/stats
mv *_assessment.tsv ${TYPE}/k${KMER}/details
mv clusters*tsv ${TYPE}/k${KMER}/clusters
rm *namesMap *relations.tsv min*

# Visualize
cd ${TYPE}/k${KMER}/summaries
find *txt | sort -V | xargs grep "" | python ../../../../../scripts/visualize_kClusters_clustering.py kCluster_k${kmer}.html
mv kCluster_k${kmer}.html ../visualization/
