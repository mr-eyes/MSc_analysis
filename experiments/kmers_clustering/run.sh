#!/bin/bash

FILTER=../../scripts/filter_by_length.py
CLUSTER=../../scripts/kallisto_kmer_clustering.py
ASSESS=../../scripts/kallisto_assess_by_gene.py
KALLISTO=kallisto
FASTA=$(sed "s/.*\///" <<< $1)
KMER=$2

python $FILTER $1 filtered_K${KMER} ${KMER}
./${KALLISTO} index -i ${KMER}.idx filtered_K${KMER}_${FASTA} -k ${KMER}
./${KALLISTO} inspect ${KMER}.idx --gfa=${KMER}.gfa
rm *idx
python $CLUSTER ${KMER}.gfa clusters_k${KMER}.tsv
rm *gfa
python $ASSESS filtered_K${KMER}* clusters_k${KMER}.tsv k${KMER}_clusters_assessment.tsv
rm filtered_K${KMER}_${FASTA}
mkdir K${KMER}_assessement
mv *.tsv K${KMER}_assessement/
mv *summary* K${KMER}_assessement/
mv *stats.json K${KMER}_assessement/