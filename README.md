####  Clone
```sh
git clone --recursive https://github.com/mr-eyes/master-analysis
cd master-analysis/
```
#### Build CD-HIT 
```sh
bash build_cdhit.sh
```
####  Data preparation
```sh
mkdir data
cd data/

#1 Download Human Transcriptome
wget -c ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_28/gencode.v28.transcripts.fa.gz

#2 Download GTF: Comprehensive gene annotation | PRI
ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_28/gencode.v28.primary_assembly.annotation.gtf.gz

#3 Extract files
gunzip *

#4 Generate protein_coding sequences
python ../scripts/filter_multifasta.py gencode.v28.transcripts.fa protein_coding

#5 Adding gene locus to human transcriptome fasta headers
python ../scripts/add_locus.py -i gencode.v28.transcripts.fa -g gencode.v28.primary_assembly.annotation.gtf -o loci_gencode.v28.transcripts.fa

#6 Adding gene locus to protein coding transcripts fasta headers
python ../scripts/add_locus.py -i protein_coding_gencode.v28.transcripts.fa -g gencode.v28.primary_assembly.annotation.gtf -o loci_protein_coding_gencode.v28.transcripts.fa
```
####  Data Exploration
```sh
mkdir overview; cd overview/
#1 Generating Histogram
python ../../scripts/histogram.py ../gencode.v28.transcripts.fa

#2 Replicating gencode stats | RNA Types count
python ../../scripts/extract_RNA_types.py ../gencode.v28.transcripts.fa > rna_types.txt

#3 Get stats about the GTF
python ../../scripts/gtf_stats.py ../gencode.v28.primary_assembly.annotation.gtf > gtf_stats.txt

# Move to root directory
cd ../../
```
####   Kallisto Kmer-based partitioning experiments
```sh
cd experiments/kmers_clustering/

#1 Download Kallisto executable file from "https://github.com/pachterlab/kallisto/releases"
https://github.com/pachterlab/kallisto/releases/download/v0.44.0/kallisto_linux-v0.44.0.tar.gz

#2 Extract and rename
tar -xzf kallisto_linux-v0.44.0.tar.gz
rm *gz
mv kallisto_linux-v0.44.0/kallisto ./
rm -rf kallisto_linux-v0.44.0

```
####  
```sh

```
####  
```sh

```
####  
```sh

```
####  
```sh

```
####  
```sh

```
