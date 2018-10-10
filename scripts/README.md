# Scripts

## Histogram

- **Description:** Draw histogram of sequence lengths Vs. Number of occurence.

- **Run:**  `python histogram.py <Fasta_file> <optional: seq_length_threshold>`

- Ex: `python histogram.py 100` will plot only sequences with length <= 100 bp

## Add gene locus to Fasta headers

- **Description:** Parse GTF file to generate list of gene loci from the overlaping genes intervals then append the gene locus ID to the transcript fasta header.

- **Run:**  `python add_locus.py -i <ORIGINAL_FASTA> -g <GTF_FILE> -o <OUTPUT_FASTA>`

- Ex: `python add_locus.py -i tr.fa -g tr.gtf -o out.fa`

## Add gene type to Fasta headers

- **Description:** Parse GTF file to generate list of genes types then append the gene type to the transcript fasta header.

- **Run:**  `python add_genetype.py -i <ORIGINAL_FASTA> -g <GTF_FILE> -o <OUTPUT_FASTA>`

- Ex: `python add_genetype.py -i tr.fa -g tr.gtf -o out.fa`

## CD-HIT Clustering Assessment

- **Description:** Ask two questions for every cluster to assess the clustering quality.

- **Run:**  `python cdhit_assess_by_gene.py <fasta_file> <clstr_file> <output_file>`

- Ex: `python clusters_assessment.py tr.fa exp.clstr`

## Kallisto GFA kmer-based Clustering

- **Description:** Convert kallisto GFA generated graph file to clusters TSV file.

- **Run:**  `python kallisto_kmer_clustering.py <GFA_file>`

- Ex: `python  kallisto_kmer_clustering.py x.gfa`

## Kallisto Cluster assissment

- **Description:** Process the previous script output with the fasta file for clustering assessment.

- **Run:**  `python kallisto_assess_by_gene.py <FASTA_file> <GFA_file> <output_file>`

- Ex: `python clusters_assessment.py tr.fa res.tsv assessement.tsv`
  
## GTF Statistics

- **Description:** Ask two questions for every cluster to assess the clustering quality.

- **Run:**  `python gtf_stats.py <GTF_file>`

- Ex: `python gtf_stats.py chr.gtf`

## Sequences filteration with length threshold

- **Description:** Write new fasta file with sequences has lengths more than threshold.

- **Run:**  `python filter_by_length.py <fasta_file> <output_fasta_file> <length_threshold>`

- Ex: `python filter_by_length.py original.fasta filtered.fasta 200`

## Sequences filteration of specific transcript type

- **Description:** Generate new fasta file with only selected transcript types.

- **Run:**  `python filter_multifasta.py <fasta_file> <rna_type(s)>`

- Ex: `python filter_multifasta.py transcriptome.fa protein_coding`

## Visualizting CD-HIT clustering assessment results

- **Description:** Export HTML page with graph visualizing clustering assessement results.

- **Run:**  `grep "" <summary_files*> | python visualize_cdhit_clustering.py <HTML file_name>`

- Ex: `grep "" */*summary* | python visualize_cdhit_clustering.py cd_hit.html`

## Visualizting Kallisto kmer-based clustering assessment results

- **Description:** Export HTML page with graph visualizing clustering assessement results.

- **Run:**  `grep "" <summary_files*> | python visualize_kmers_clustering.py <HTML file_name>`

- Ex: `grep "" */*summary* | python visualize_kmers_clustering.py kallisto_kmers.html`