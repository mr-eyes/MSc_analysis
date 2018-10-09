#!/bin/bash

FILTER=../../scripts/filter_by_length.py
CLUSTER=../../scripts/kallisto_kmer_clustering.py
ASSESS=../../scripts/kallisto_assess_by_gene.py
KALLISTO=kallisto/build/src/kallisto
FASTA=$(sed "s/.*\///" <<< $1)
KMER=$2
TYPE=$3
# Filteration of any sequence with length more than Kmer-Size
python $FILTER $1 filtered_K${KMER} ${KMER}

# Generating kallisto index then GFA
./${KALLISTO} index -i ${KMER}.idx filtered_K${KMER}_${FASTA} -k ${KMER}
./${KALLISTO} inspect ${KMER}.idx --gfa=${KMER}.gfa

# Delete Kallisto Index
rm *idx

# Perform Clustering of Kallisto's GFA Output
python $CLUSTER ${KMER}.gfa clusters_k${KMER}.tsv

# Delete the GFA file
rm *gfa

# Perform Clustering Assessment and save output files
python $ASSESS filtered_K${KMER}* clusters_k${KMER}.tsv k${KMER}_clusters_assessment.tsv

rm filtered_K${KMER}_${FASTA}

mkdir -p ${TYPE}_results/K${KMER}_assessement
mv *.tsv ${TYPE}_results/K${KMER}_assessement/
mv *summary* ${TYPE}_results/K${KMER}_assessement/
mv *stats.json ${TYPE}_results/K${KMER}_assessement/