# Scripts

## Histogram
- **Description:** Draw histogram of sequence lengths Vs. Number of occurence.
- **Run:** `python histogram.py [seq_length_threshold]`
	- Ex: `python histogram.py 100` will plot only sequences with length <= 100 bp

## Add gene locus to Fasta headers
- **Description:** Parse GTF file to generate list of gene loci from the overlaping genes intervals then append the gene locus ID to the transcript fasta header.
- **Run:** `python add_locus.py [-i ORIGINAL_FASTA] [-g GTF_FILE] [-o OUTPUT_FASTA]` 
	- Ex: `python add_locus.py -i tr.fa -g tr.gtf -o out.fa`

## Add gene type to Fasta headers
- **Description:** Parse GTF file to generate list of genes types then append the gene type to the transcript fasta header.
- **Run:** `python add_genetype.py [-i ORIGINAL_FASTA] [-g GTF_FILE] [-o OUTPUT_FASTA]` 
	- Ex: `python add_genetype.py -i tr.fa -g tr.gtf -o out.fa`


## 	CD-HIT Clustering Assessment
- **Description:** Ask two questions for every cluster to assess the clustering quality.
- **Run:** `python clusters_assessment.py [fasta_file] [clstr_file]` 
	- Ex: `python clusters_assessment.py tr.fa exp.clstr`


## GTF Statistics
- **Description:** Ask two questions for every cluster to assess the clustering quality.
- **Run:** `python gtf_stats.py [GTF_file]` 
	- Ex: `python gtf_stats.py chr.gtf`
